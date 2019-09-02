from .helpers import create_data_frame
from .trend import Trend


class Evaluator:
    def __init__(self, price_data):
        self.data_frame = create_data_frame(price_data)

    def evaluate_price(self, current_price):
        last_row = self.data_frame.iloc[-1]
        last_moving_ave = last_row["ma"]
        last_moving_ave_smooth = last_row["ma_dy_smooth"]

        if Evaluator._get_trend(last_moving_ave_smooth) == Trend.UP:
            # upwards trend mode
            # go long when the price hits the moving average, exit when it hits the upper BB
            if current_price <= last_moving_ave:
                return "BUY"

        if Evaluator._get_trend(last_moving_ave_smooth) == Trend.DOWN:
            # downwards trend mode
            # go short when the price hits the MA, exit when it hits the lower BB
            if current_price >= last_moving_ave:
                return "SELL"

        return None

    @staticmethod
    def _get_trend(current_moving_ave_smooth):
        if current_moving_ave_smooth > 0.01:
            return Trend.UP
        if current_moving_ave_smooth < -0.01:
            return Trend.DOWN

        return Trend.NONE
