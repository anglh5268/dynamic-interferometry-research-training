import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from src.phase_processing import (
    decode_wrapped_phase,
    generate_four_step_images,
    height_to_phase,
    phase_to_height,
    unwrap_phase_sequential,
    wrap_phase,
)
from src.polarization import create_opposite_circular_fields, project_to_analyzer
from src.surfaces import create_gaussian_surface

wavelength_m = 632.8e-9
background = 1.0
contrast = 0.8
height_peak_m = 800e-9

intensity_o = 1.6
intensity_r = 0.4

x, y, height_true = create_gaussian_surface(256, 256, height_peak_m, 0.25)
phase_true = height_to_phase(height_true, wavelength_m)
jones_object, jones_reference = create_opposite_circular_fields(phase_true, intensity_o, intensity_r)

analyzer_angles = [0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

jones_channel = []

for theta_rad in analyzer_angles:
    a_object = project_to_analyzer(jones_object, theta_rad)
    a_reference = project_to_analyzer(jones_reference, theta_rad)

    i_jones = np.abs(a_object + a_reference) ** 2

    jones_channel.append(i_jones)

i_0, i_45, i_90, i_135 = jones_channel
# 参考理想光强
i1, i2, i3, i4 = generate_four_step_images(phase_true, background, contrast)
error_i_1 = i_0 - i1
error_i_2 = i_45 - i2
error_i_3 = i_90 - i3
error_i_4 = i_135 - i4

#解码光强出相位
decoded_phase = decode_wrapped_phase(i_0, i_45, i_90, i_135)
#理论相位
phase_wrapped_theory = wrap_phase(phase_true)
# 计算误差
wrapped_error = wrap_phase(decoded_phase - phase_wrapped_theory)
print("Wrapped phase abs error maximum:", np.abs(wrapped_error).max())
print("RMSE of wrapped phase error:", (wrapped_error**2).mean() ** 0.5)

# 绘制 Jones 解调包裹相位图
fig_wrapped_jones, ax_wrapped_jones = plt.subplots(figsize=(6, 5), layout="constrained")
image_wrapped_jones = ax_wrapped_jones.imshow(decoded_phase, cmap="twilight", vmin=-np.pi, vmax=np.pi, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_wrapped_jones.set_title("Jones Decoded Wrapped Phase")
fig_wrapped_jones.colorbar(image_wrapped_jones, ax=ax_wrapped_jones, label="Phase (radians)")

# 展开相位并计算活塞项
phase_unwrapped_jones = unwrap_phase_sequential(decoded_phase)
piston = np.mean(phase_unwrapped_jones - phase_true)
phase_unwrapped_aligned = phase_unwrapped_jones - piston
phase_error = phase_unwrapped_aligned - phase_true
height_recovered = phase_to_height(phase_unwrapped_aligned, wavelength_m)
height_error = height_recovered - height_true

# 展开相位补充活塞项误差计算
print("Piston (radians):", piston)
print("Phase RMSE (radians):", np.sqrt(np.mean(phase_error**2)))
print("Maximum absolute phase error (radians):", np.max(np.abs(phase_error)))
print("Recovered height maximum (m):", height_recovered.max())
print("Height RMSE (m):", np.sqrt(np.mean(height_error**2)))
print("Maximum absolute height error (m):", np.max(np.abs(height_error)))

# 四步相移图
fig_intensities, ax_intensities = plt.subplots(2, 2)
image_intensity = ax_intensities[0, 0].imshow(
    i_0,
    cmap="gray",
    vmin=background - contrast,
    vmax=background + contrast,
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_intensities[0, 0].set_title("I1")
ax_intensities[0, 1].imshow(
    i_45,
    cmap="gray",
    vmin=background - contrast,
    vmax=background + contrast,
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_intensities[0, 1].set_title("I2")
ax_intensities[1, 0].imshow(
    i_90,
    cmap="gray",
    vmin=background - contrast,
    vmax=background + contrast,
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_intensities[1, 0].set_title("I3")
ax_intensities[1, 1].imshow(
    i_135,
    cmap="gray",
    vmin=background - contrast,
    vmax=background + contrast,
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_intensities[1, 1].set_title("I4")
fig_intensities.colorbar(image_intensity, ax=ax_intensities, label="Intensity (a.u.)")

# 高度计算并画图
height_true_nm = height_true * 1e9
height_recovered_nm = height_recovered * 1e9
height_error_recovered = height_error * 1e22
error_limit_height = np.max(np.abs(height_error_recovered))

fig_height, ax_height = plt.subplots(1, 3, figsize=(14, 4), layout="constrained")
image_height_real = ax_height[0].imshow(
    height_true_nm,
    cmap="viridis",
    vmin=height_true_nm.min(),
    vmax=height_true_nm.max(),
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_height[0].set_title("True Height")

ax_height[1].imshow(
    height_recovered_nm,
    cmap="viridis",
    vmin=height_true_nm.min(),
    vmax=height_true_nm.max(),
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_height[1].set_title("Recovered Height")

fig_height.colorbar(image_height_real, ax=ax_height[:2], label="height(nm)")

image_height_error = ax_height[2].imshow(
    height_error_recovered,
    cmap="coolwarm",
    vmin=-error_limit_height,
    vmax=error_limit_height,
    origin="lower",
    extent=[x.min(), x.max(), y.min(), y.max()],
    aspect="equal",
)
ax_height[2].set_title("Height Error")

fig_height.colorbar(image_height_error, ax=ax_height[2], label="error(1e-22m)")

# 中心剖面对比
center_row = np.argmin(np.abs(y))
true_profile_nm = height_true[center_row, :] * 1e9
recovered_profile_nm = height_recovered[center_row, :] * 1e9
error_profile_scaled = height_error[center_row, :] * 1e22

fig_profile, ax_profile = plt.subplots(1, 2, figsize=(12, 4), layout="constrained")
ax_profile[0].plot(x, true_profile_nm, label="True height")
ax_profile[0].plot(x, recovered_profile_nm, label="Recovered height")
ax_profile[0].set_xlabel("Normalized X")
ax_profile[0].set_ylabel("Height (nm)")
ax_profile[0].legend()
ax_profile[0].grid()
ax_profile[0].set_title("Center Height Profile")

ax_profile[1].plot(x, error_profile_scaled, label="Height error")
ax_profile[1].axhline(0, color="black", linestyle="--")
ax_profile[1].set_xlabel("Normalized X")
ax_profile[1].set_ylabel("Height error (1e-22 m)")
ax_profile[1].legend()
ax_profile[1].grid()
ax_profile[1].set_title("Center Height Error Profile")

# 保存图片
project_root = Path(__file__).resolve().parents[1]
case_b_dir = project_root / "results" / "case_b_jones_ideal"
figures_dir = case_b_dir / "figures"
metrics_dir = case_b_dir / "metrics"
metrics_json_path = metrics_dir / "case_b_jones_metrics.json"

figures_dir.mkdir(parents=True, exist_ok=True)
metrics_dir.mkdir(parents=True, exist_ok=True)

fig_intensities.savefig(figures_dir / "01_jones_four_channel_intensities.png", dpi=300, bbox_inches="tight")
fig_wrapped_jones.savefig(figures_dir / "02_jones_wrapped_phase.png", dpi=300, bbox_inches="tight")
fig_height.savefig(figures_dir / "03_jones_height_recovery.png", dpi=300, bbox_inches="tight")
fig_profile.savefig(figures_dir / "04_jones_center_profile.png", dpi=300, bbox_inches="tight")

# 保存相应参数
parameters = {
    "wavelength_m": float(wavelength_m),
    "background": float(background),
    "contrast": float(contrast),
    "height_peak_m": float(height_peak_m),
}
sampling_check = {
    "max_true_phase_rad": float(phase_true.max()),
    "max_adjacent_diff_x_rad": float(np.max(np.abs(np.diff(phase_true, axis=1)))),
    "max_adjacent_diff_y_rad": float(np.max(np.abs(np.diff(phase_true, axis=0)))),
    "x_sampling_valid": bool(np.max(np.abs(np.diff(phase_true, axis=1))) < np.pi),
    "y_sampling_valid": bool(np.max(np.abs(np.diff(phase_true, axis=0))) < np.pi),
}

wrapped_phase_validation = {
    "max_circular_error_rad": float(np.max(np.abs(wrapped_error))),
    "rmse_circular_error_rad": float(np.sqrt(np.mean(wrapped_error**2))),
}
unwrapped_reconstruction = {
    "piston_rad": float(piston),
    "phase_rmse_rad": float(np.sqrt(np.mean(phase_error**2))),
    "max_absolute_phase_error_rad": float(np.max(np.abs(phase_error))),
    "recovered_height_max_m": float(height_recovered.max()),
    "height_rmse_m": float(np.sqrt(np.mean(height_error**2))),
    "max_absolute_height_error_m": float(np.max(np.abs(height_error))),
    "true_height_pv_m": float(height_true.max() - height_true.min()),
    "recovered_height_pv_m": float(height_recovered.max() - height_recovered.min()),
    "height_error_pv_m": float(height_error.max() - height_error.min()),
}

metrics = {
    "case_name": "case_b_ideal_jones_four_channel",
    "parameters": parameters,
    "sampling_check": sampling_check,
    "wrapped_phase_validation": wrapped_phase_validation,
    "unwrapped_reconstruction": unwrapped_reconstruction,
}

with metrics_json_path.open("w", encoding="utf-8") as file:
    json.dump(metrics, file, ensure_ascii=False, indent=2)

plt.show()
