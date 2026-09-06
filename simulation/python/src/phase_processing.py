import numpy as np


def height_to_phase(height_m, wavelength_m):
    # 高度转换相位
    if wavelength_m <= 0:
        raise ValueError("Wavelength must be positive.")
    return (4 * np.pi / wavelength_m) * height_m

def generate_four_step_images(phase_rad, background, contrast):
    if not (0 <= background):
        raise ValueError("Background must be a non-negative value.")
    if not (0 <= contrast <= background):
        raise ValueError("Contrast must be between 0 and the background value.")
    # 计算四步相移干涉图像
    I1 = background + contrast * np.cos(phase_rad)
    I2 = background + contrast * np.cos(phase_rad + np.pi / 2)
    I3 = background + contrast * np.cos(phase_rad + np.pi)
    I4 = background + contrast * np.cos(phase_rad + 3 * np.pi / 2)
    return I1, I2, I3, I4

def decode_wrapped_phase(I1, I2, I3, I4):
    # 解码相位
    if I1.shape != I2.shape or I1.shape != I3.shape or I1.shape != I4.shape:
        raise ValueError("All input images must have the same shape.")
    numerator = I4 - I2
    denominator = I1 - I3
    wrapped_phase = np.arctan2(numerator, denominator)
    return wrapped_phase

def phase_to_height(phase_rad, wavelength_m):
    # 相位转换高度
    if wavelength_m <= 0:
        raise ValueError("Wavelength must be positive.")
    return (phase_rad * wavelength_m) / (4 * np.pi)

def wrap_phase(phase_rad):
    # 将相位包裹到[-π, π]范围内
    return np.angle(np.exp(1j * phase_rad))

def unwrap_phase_sequential(wrapped_phase):
    # 相位展开
    if wrapped_phase.ndim != 2:
        raise ValueError("Input wrapped phase must be a 2D array.")
    phase_unwrapped = np.unwrap(wrapped_phase, axis=0)
    phase_unwrapped = np.unwrap(phase_unwrapped, axis=1)
    return phase_unwrapped
