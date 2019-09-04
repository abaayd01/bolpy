from .helpers import create_data_frame
from .trend import Trend


class Evaluator:
    def __init__(self, price_data):
        self.data_frame = create_data_frame(price_data)
        self._init_last_moving_averages()
        self._init_trend()

    def _init_last_moving_averages(self):
        last_row = self.data_frame.iloc[-1]
        self.last_moving_ave = last_row["ma"]
        self.last_moving_ave_smooth = last_row["ma_dy_smooth"]

    def _init_trend(self):
        self.trend = Evaluator._get_trend(self.last_moving_ave_smooth)

    @staticmethod
    def _get_trend(current_moving_ave_smooth):
        if current_moving_ave_smooth > 0.01:
            return Trend.UP
        if current_moving_ave_smooth < -0.01:
            return Trend.DOWN

        return Trend.NONE

    @staticmethod
    def eval_test():
        return "BUY"

    def evaluate_price(self, current_price):
        # upwards trend mode
        # go long when the price hits the moving average, exit when it hits the upper BB
        if self._is_trending_up() and current_price <= self.last_moving_ave:
            return "BUY"

        # downwards trend mode
        # go short when the price hits the MA, exit when it hits the lower BB
        if self._is_trending_down() and current_price >= self.last_moving_ave:
            return "SELL"

        return None

    def _is_trending_up(self):
        if self.trend == Trend.UP:
            return True

        return False

    def _is_trending_down(self):
        if self.trend == Trend.DOWN:
            return True

        return False
