import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from src.dynamic import (
    center_symmetric_sample_times,
    generate_dynamic_four_step_images,
    sinusoidal_phase,
)
from src.phase_processing import (
    decode_wrapped_phase,
    height_to_phase,
    phase_to_height,
    unwrap_phase_sequential,
    wrap_phase,
)
from src.surfaces import create_gaussian_surface


WAVELENGTH_M = 632.8e-9
BACKGROUND = 1.0
CONTRAST = 0.8
HEIGHT_PEAK_M = 800e-9
FRAME_INTERVAL_S = 1e-3
CENTER_TIME_S = 0.0


def align_only_2pi_branch(phase_unwrapped, phase_truth):
    mean_difference = np.mean(phase_unwrapped - phase_truth)
    branch = np.round(mean_difference / (2 * np.pi)) * (2 * np.pi)
    return phase_unwrapped - branch, float(branch)


def calculate_metrics(decoded_wrapped, phase_truth):
    circular_error = wrap_phase(decoded_wrapped - wrap_phase(phase_truth))
    phase_unwrapped = unwrap_phase_sequential(decoded_wrapped)
    phase_aligned, branch_shift = align_only_2pi_branch(
        phase_unwrapped, phase_truth
    )
    phase_error = phase_aligned - phase_truth
    shape_error = phase_error - np.mean(phase_error)
    height_error = phase_to_height(phase_error, WAVELENGTH_M)
    return {
        "decoded_wrapped": decoded_wrapped,
        "phase_aligned": phase_aligned,
        "phase_error": phase_error,
        "shape_error": shape_error,
        "circular_rmse_rad": float(np.sqrt(np.mean(circular_error**2))),
        "circular_max_abs_rad": float(np.max(np.abs(circular_error))),
        "absolute_phase_rmse_rad": float(np.sqrt(np.mean(phase_error**2))),
        "mean_phase_error_rad": float(np.mean(phase_error)),
        "shape_phase_rmse_rad": float(np.sqrt(np.mean(shape_error**2))),
        "equivalent_height_rmse_m": float(
            np.sqrt(np.mean(height_error**2))
        ),
        "branch_shift_rad": branch_shift,
    }


def run_case(base_phase, amplitude_rad, q_rad_per_frame, beta_rad):
    omega = q_rad_per_frame / FRAME_INTERVAL_S
    sequential_times = center_symmetric_sample_times(
        CENTER_TIME_S, FRAME_INTERVAL_S
    )
    synchronous_times = np.full(4, CENTER_TIME_S)
    truth = sinusoidal_phase(
        base_phase,
        CENTER_TIME_S,
        amplitude_rad,
        omega,
        beta_rad,
    )
    sequential_images = generate_dynamic_four_step_images(
        base_phase,
        sequential_times,
        BACKGROUND,
        CONTRAST,
        amplitude_rad,
        omega,
        beta_rad,
    )
    synchronous_images = generate_dynamic_four_step_images(
        base_phase,
        synchronous_times,
        BACKGROUND,
        CONTRAST,
        amplitude_rad,
        omega,
        beta_rad,
    )
    sequential = calculate_metrics(
        decode_wrapped_phase(*sequential_images), truth
    )
    synchronous = calculate_metrics(
        decode_wrapped_phase(*synchronous_images), truth
    )
    return truth, sequential, synchronous


def scalar_metrics(result):
    return {
        key: value
        for key, value in result.items()
        if not isinstance(value, np.ndarray)
    }


def sweep_one_parameter(base_phase, values, parameter):
    results = []
    defaults = {
        "amplitude_rad": 1.0,
        "q_rad_per_frame": np.pi / 3,
        "beta_rad": np.pi / 4,
    }
    for value in values:
        settings = defaults | {parameter: float(value)}
        _, sequential, synchronous = run_case(base_phase, **settings)
        results.append(
            (
                sequential["absolute_phase_rmse_rad"],
                sequential["shape_phase_rmse_rad"],
                synchronous["absolute_phase_rmse_rad"],
            )
        )
    return np.asarray(results)


def main():
    x, y, height_true = create_gaussian_surface(
        num_x=256,
        num_y=256,
        height_peak_m=HEIGHT_PEAK_M,
        sigma_normalized=0.25,
    )
    base_phase = height_to_phase(height_true, WAVELENGTH_M)

    representative = {
        "amplitude_rad": 1.0,
        "q_rad_per_frame": np.pi / 3,
        "beta_rad": np.pi / 4,
    }
    truth, sequential, synchronous = run_case(base_phase, **representative)

    project_root = Path(__file__).resolve().parents[1]
    result_dir = project_root / "results" / "dynamic_global_ideal"
    figures_dir = result_dir / "figures"
    metrics_dir = result_dir / "metrics"
    figures_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir.mkdir(parents=True, exist_ok=True)

    extent = [x.min(), x.max(), y.min(), y.max()]
    error_limit = max(
        np.max(np.abs(sequential["phase_error"])),
        np.finfo(float).eps,
    )
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), layout="constrained")
    phase_limits = (truth.min(), truth.max())
    fields = [
        (truth, "Center-time truth", "viridis", *phase_limits),
        (
            sequential["phase_aligned"],
            "Sequential recovery",
            "viridis",
            *phase_limits,
        ),
        (
            synchronous["phase_aligned"],
            "Synchronous recovery",
            "viridis",
            *phase_limits,
        ),
        (
            sequential["phase_error"],
            "Sequential absolute error",
            "coolwarm",
            -error_limit,
            error_limit,
        ),
        (
            sequential["shape_error"],
            "Sequential shape error",
            "coolwarm",
            -error_limit,
            error_limit,
        ),
        (
            synchronous["phase_error"],
            "Synchronous error",
            "coolwarm",
            -error_limit,
            error_limit,
        ),
    ]
    for axis, (data, title, cmap, vmin, vmax) in zip(axes.flat, fields):
        image = axis.imshow(
            data,
            origin="lower",
            extent=extent,
            aspect="equal",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
        )
        axis.set_title(title)
        fig.colorbar(image, ax=axis, label="Phase (rad)")
    fig.savefig(
        figures_dir / "01_representative_comparison.png",
        dpi=250,
        bbox_inches="tight",
    )
    plt.close(fig)

    sweep_values = {
        "amplitude_rad": np.linspace(0, np.pi, 41),
        "q_rad_per_frame": np.linspace(0, np.pi, 41),
        "beta_rad": np.linspace(0, 2 * np.pi, 49, endpoint=False),
    }
    sweep_results = {
        name: sweep_one_parameter(base_phase[::4, ::4], values, name)
        for name, values in sweep_values.items()
    }
    labels = {
        "amplitude_rad": r"Vibration amplitude $\alpha$ (rad)",
        "q_rad_per_frame": r"Frame advance $q=\Omega\Delta t$ (rad/frame)",
        "beta_rad": r"Vibration phase $\beta$ (rad)",
    }
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), layout="constrained")
    for axis, (name, values) in zip(axes, sweep_values.items()):
        data = sweep_results[name]
        axis.plot(values, data[:, 0], label="Sequential absolute RMSE")
        axis.plot(values, data[:, 1], label="Sequential shape RMSE")
        axis.plot(values, data[:, 2], "--", label="Synchronous absolute RMSE")
        axis.set_xlabel(labels[name])
        axis.set_ylabel("Phase RMSE (rad)")
        axis.grid(True, alpha=0.3)
    axes[0].legend(fontsize=8)
    fig.savefig(
        figures_dir / "02_parameter_sweeps.png",
        dpi=250,
        bbox_inches="tight",
    )
    plt.close(fig)

    metrics = {
        "case_name": "ideal_global_sinusoidal_dynamic_phase",
        "model": "phi(x,y,t)=phi0(x,y)+alpha*sin(Omega*t+beta)",
        "parameters": {
            "wavelength_m": WAVELENGTH_M,
            "background": BACKGROUND,
            "contrast": CONTRAST,
            "height_peak_m": HEIGHT_PEAK_M,
            "frame_interval_s": FRAME_INTERVAL_S,
            **representative,
            "frequency_hz": representative["q_rad_per_frame"]
            / (2 * np.pi * FRAME_INTERVAL_S),
        },
        "sample_times_s": center_symmetric_sample_times(
            CENTER_TIME_S, FRAME_INTERVAL_S
        ).tolist(),
        "truth_time_s": CENTER_TIME_S,
        "sequential": scalar_metrics(sequential),
        "synchronous": scalar_metrics(synchronous),
        "sweeps": {
            name: {
                "values": values.tolist(),
                "sequential_absolute_rmse_rad": sweep_results[name][
                    :, 0
                ].tolist(),
                "sequential_shape_rmse_rad": sweep_results[name][
                    :, 1
                ].tolist(),
                "synchronous_absolute_rmse_rad": sweep_results[name][
                    :, 2
                ].tolist(),
            }
            for name, values in sweep_values.items()
        },
    }
    with (metrics_dir / "dynamic_global_metrics.json").open(
        "w", encoding="utf-8"
    ) as file:
        json.dump(metrics, file, ensure_ascii=False, indent=2)

    print(json.dumps({
        "sequential": metrics["sequential"],
        "synchronous": metrics["synchronous"],
    }, indent=2))


if __name__ == "__main__":
    main()

