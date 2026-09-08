import numpy as np


def analyer_vector(thera_rad):
    # 生成向量
    return np.array([np.cos(thera_rad), np.sin(thera_rad)], dtype=complex)


def project_to_analyzer(jones_field, theta_rad):
    # 计算复振幅
    analyzer = analyer_vector(theta_rad)

    return (
        np.conjugate(analyzer[0]) * jones_field[0]
        + np.conjugate(analyzer[1]) * jones_field[1]
    )


def create_opposite_circular_fields(phase_rad, intensity_object, intensity_reference):
    # 构建圆偏振物光参考光矢量
    phase_rad = np.asarray(phase_rad)
    object_amplitude = np.sqrt(intensity_object) * np.exp(1j * phase_rad) / np.sqrt(2)
    reference_amplitude = (
        np.sqrt(intensity_reference)
        * np.ones_like(phase_rad, dtype=complex)
        / np.sqrt(2)
    )

    jones_object = np.stack([object_amplitude, 1j * object_amplitude], axis=0)
    jones_reference = np.stack([reference_amplitude, -1j * reference_amplitude], axis=0)

    return jones_object, jones_reference
