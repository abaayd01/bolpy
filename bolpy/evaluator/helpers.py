import pandas as pd
import numpy as np


def create_data_frame(price_data):
    price_df = pd.DataFrame({'price': price_data})
    price_df = format_data(price_df)
    return price_df


def format_data(data_frame):
    window_size = 10
    bol_multiplier = 2

    data_frame = append_moving_average(data_frame, window_size)
    data_frame = append_moving_average_diff(data_frame)
    data_frame = smooth_moving_average_diff(data_frame, window_size)
    data_frame = append_std_dev(data_frame, window_size)
    data_frame = append_bol_bands(data_frame, bol_multiplier)

    return data_frame


def append_moving_average(data_frame, window_size):
    moving_average = data_frame["price"].rolling(window=window_size).mean()
    data_frame = data_frame.assign(ma=moving_average)
    return data_frame


def append_moving_average_diff(data_frame):
    ma_dy = np.diff(data_frame["ma"])
    ma_dy = np.insert(ma_dy, 0, [0])
    data_frame = data_frame.assign(ma_dy=ma_dy)
    return data_frame


def smooth_moving_average_diff(data_frame, window_size):
    smooth_diff_moving_average = data_frame["ma_dy"].rolling(window=window_size).mean()
    data_frame = data_frame.assign(ma_dy_smooth=smooth_diff_moving_average)
    return data_frame


def append_std_dev(data_frame, window_size):
    moving_average = data_frame["price"].rolling(window=window_size).std()
    data_frame = data_frame.assign(std=moving_average)
    return data_frame


def append_bol_bands(data_frame, bol_multiplier):
    data_frame["bol_lower"] = data_frame["ma"] - bol_multiplier * data_frame["std"]
    data_frame["bol_upper"] = data_frame["ma"] + bol_multiplier * data_frame["std"]
    return data_frame
