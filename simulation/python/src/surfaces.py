import numpy as np


def create_gaussian_surface(
        num_x,
        num_y,
        height_peak_m,
        sigma_normalized,
):
    # 创建高斯平面
    x = np.linspace(-1, 1, num_x)
    y = np.linspace(-1, 1, num_y)
    #X, Y是二维的 类似于矩阵 那可推出height_true也是二维的
    X, Y = np.meshgrid(x, y)

    radius_squared = X**2 + Y**2
    exponent = -radius_squared / (2 * sigma_normalized**2)
    height_true = height_peak_m * np.exp(exponent)

    return x, y, height_true
