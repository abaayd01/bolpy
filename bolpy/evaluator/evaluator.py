from .helpers import create_data_frame
from .trend import Trend
from bolpy.proto import bol_pb2


class Evaluator:
    def __init__(self, price_data):
        self.stop_loss_percent = 0.02
        self.data_frame = create_data_frame(price_data)
        self._init_last_moving_averages()
        self._init_trend()

    def _init_last_moving_averages(self):
        self.last_row = self.data_frame.iloc[-1]
        self.last_moving_ave = self.last_row["ma"]
        self.last_moving_ave_smooth = self.last_row["ma_dy_smooth"]

    def _init_trend(self):
        self.trend = Evaluator._get_trend(self.last_moving_ave_smooth)

    @staticmethod
    def _get_trend(current_moving_ave_smooth):
        if current_moving_ave_smooth > 0.01:
            return Trend.UP
        if current_moving_ave_smooth < -0.01:
            return Trend.DOWN

        return Trend.NONE

    def evaluate_price(self, current_price):
        # upwards trend mode
        # go long when the price hits the moving average, exit when it hits the upper BB
        if self._is_trending_up() and current_price <= self.last_moving_ave:
            return self._form_price_evaluation_response("BUY", current_price)

        # downwards trend mode
        # go short when the price hits the MA, exit when it hits the lower BB
        if self._is_trending_down() and current_price >= self.last_moving_ave:
            return self._form_price_evaluation_response("SELL", current_price)

        return bol_pb2.PriceEvaluationResponse(action="NONE")

    def _form_price_evaluation_response(self, action, current_price):
        return bol_pb2.PriceEvaluationResponse(
            action=action,
            evaluationPrice=current_price,
            targetExitPrice=self._get_target_exit_price(action),
            stopLossPrice=self._calculate_stop_loss(action),
            bolUpper=self._get_bol_upper(),
            bolLower=self._get_bol_lower(),
            movingAverage=self._get_moving_average()
        )

    def _is_trending_up(self):
        if self.trend == Trend.UP:
            return True

        return False

    def _is_trending_down(self):
        if self.trend == Trend.DOWN:
            return True

        return False

    def _get_target_exit_price(self, action):
        if action == "BUY":
            return self._get_bol_upper()

        if action == "SELL":
            return self._get_bol_lower()

        return None

    def _calculate_stop_loss(self, action):
        if action == "BUY":
            return self.last_moving_ave * (1 - self.stop_loss_percent)

        if action == "SELL":
            return self.last_moving_ave * (1 + self.stop_loss_percent)

        return None

    def _get_bol_upper(self):
        return self.last_row["bol_upper"]

    def _get_bol_lower(self):
        return self.last_row["bol_lower"]

    def _get_moving_average(self):
        return self.last_moving_ave
