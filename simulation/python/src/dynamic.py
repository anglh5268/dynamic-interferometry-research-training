import numpy as np


FOUR_STEP_SHIFTS_RAD = np.arange(4, dtype=float) * (np.pi / 2)


def sinusoidal_phase(
    base_phase_rad,
    time_s,
    amplitude_rad,
    angular_frequency_rad_s,
    initial_phase_rad=0.0,
    spatial_mode=None,
):
    """Evaluate a static phase plus a sinusoidal dynamic perturbation."""
    base_phase_rad = np.asarray(base_phase_rad, dtype=float)
    if base_phase_rad.ndim != 2:
        raise ValueError("base_phase_rad must be a 2D array.")
    if amplitude_rad < 0:
        raise ValueError("amplitude_rad must be non-negative.")
    if angular_frequency_rad_s < 0:
        raise ValueError("angular_frequency_rad_s must be non-negative.")

    if spatial_mode is None:
        spatial_mode = np.ones_like(base_phase_rad)
    else:
        spatial_mode = np.asarray(spatial_mode, dtype=float)
        if spatial_mode.shape != base_phase_rad.shape:
            raise ValueError("spatial_mode must match base_phase_rad.shape.")

    dynamic_scale = amplitude_rad * np.sin(
        angular_frequency_rad_s * np.asarray(time_s, dtype=float)
        + initial_phase_rad
    )
    return (
        base_phase_rad
        + dynamic_scale[..., np.newaxis, np.newaxis] * spatial_mode
    )


def generate_dynamic_four_step_images(
    base_phase_rad,
    sample_times_s,
    background,
    contrast,
    amplitude_rad,
    angular_frequency_rad_s,
    initial_phase_rad=0.0,
    spatial_mode=None,
):
    """Generate four phase-shifted images at explicitly supplied times."""
    sample_times_s = np.asarray(sample_times_s, dtype=float)
    if sample_times_s.shape != (4,):
        raise ValueError("sample_times_s must contain exactly four values.")
    if background < 0:
        raise ValueError("background must be non-negative.")
    if not 0 <= contrast <= background:
        raise ValueError("contrast must be between zero and background.")

    sampled_phase = sinusoidal_phase(
        base_phase_rad,
        sample_times_s,
        amplitude_rad,
        angular_frequency_rad_s,
        initial_phase_rad,
        spatial_mode,
    )
    images = background + contrast * np.cos(
        sampled_phase + FOUR_STEP_SHIFTS_RAD[:, np.newaxis, np.newaxis]
    )
    return tuple(images)


def center_symmetric_sample_times(center_time_s, frame_interval_s):
    """Return four sequential sample times symmetric about center_time_s."""
    if frame_interval_s < 0:
        raise ValueError("frame_interval_s must be non-negative.")
    offsets = np.array([-1.5, -0.5, 0.5, 1.5]) * frame_interval_s
    return center_time_s + offsets

