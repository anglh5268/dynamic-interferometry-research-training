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
from src.surfaces import create_gaussian_surface

wavelength_m = 632.8e-9
background = 1.0
contrast = 0.8
height_peak_m = 800e-9

# 高斯平面
x, y, height_true = create_gaussian_surface(num_x=256, num_y=256, height_peak_m=height_peak_m, sigma_normalized=0.25)
# 将高度转换为真实相位
phase_true = height_to_phase(height_true, wavelength_m)
print("Maximum true phase:", phase_true.max())
print("Maximum adjacent phase difference in x-direction:", np.max(np.abs(np.diff(phase_true, axis=1))))
print("Maximum adjacent phase difference in y-direction:", np.max(np.abs(np.diff(phase_true, axis=0))))

# 四步相移计算
i1, i2, i3, i4 = generate_four_step_images(phase_true, background, contrast)
fig_intensities, ax_intensities = plt.subplots(2, 2)
image_intensity = ax_intensities[0, 0].imshow(i1, cmap="gray", vmin=background - contrast, vmax=background + contrast, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_intensities[0, 0].set_title("I1")
ax_intensities[0, 1].imshow(i2, cmap="gray", vmin=background - contrast, vmax=background + contrast, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_intensities[0, 1].set_title("I2")
ax_intensities[1, 0].imshow(i3, cmap="gray", vmin=background - contrast, vmax=background + contrast, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_intensities[1, 0].set_title("I3")
ax_intensities[1, 1].imshow(i4, cmap="gray", vmin=background - contrast, vmax=background + contrast, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_intensities[1, 1].set_title("I4")
fig_intensities.colorbar(image_intensity, ax=ax_intensities, label="Intensity (a.u.)")

# 理论包裹相位
phase_wrapped_theory = wrap_phase(phase_true)
# 解码包裹相位
phase_wrapped_decoded = decode_wrapped_phase(i1, i2, i3, i4)
# 理论包裹相位和解码包裹相位的误差
wrapped_error = wrap_phase(phase_wrapped_decoded - phase_wrapped_theory)
print("Wrapped phase abs error maximum:", np.abs(wrapped_error).max())
print("RMSE of wrapped phase error:", (wrapped_error**2).mean() ** 0.5)

fig_wrapped_comparison, ax_wrapped_comparison = plt.subplots(1, 2)
image_wrapped_decoded = ax_wrapped_comparison[0].imshow(phase_wrapped_decoded, cmap="twilight", vmin=-np.pi, vmax=np.pi, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_wrapped_comparison[0].set_title("Decoded Wrapped Phase")

ax_wrapped_comparison[1].imshow(phase_wrapped_theory, cmap="twilight", vmin=-np.pi, vmax=np.pi, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_wrapped_comparison[1].set_title("Theoretical Wrapped Phase")

fig_wrapped_comparison.colorbar(image_wrapped_decoded, ax=ax_wrapped_comparison, label="Phase (radians)")

# 计算包裹相位得到的高度
height_from_wrapped_phase = phase_to_height(phase_wrapped_decoded, wavelength_m)
height_error_from_wrapped_phase = height_from_wrapped_phase - height_true
print("\n--- Direct conversion from wrapped phase (expected failure) ---")
print("Maximum height from wrapped phase (m):", height_from_wrapped_phase.max())
print("Wrapped-phase height RMSE (m):", np.sqrt(np.mean(height_error_from_wrapped_phase**2)))
print("Maximum absolute wrapped-phase height error (m):", np.max(np.abs(height_error_from_wrapped_phase)))

# 展开相位
phase_unwrapped = unwrap_phase_sequential(phase_wrapped_decoded)
piston = np.mean(phase_unwrapped - phase_true)
phase_unwrapped_aligned = phase_unwrapped - piston
phase_error = phase_unwrapped_aligned - phase_true
height_recovered = phase_to_height(phase_unwrapped_aligned, wavelength_m)
height_error = height_recovered - height_true

# 展开相位补充活塞项误差计算
print("\n--- After unwrapping and piston alignment ---")
print("Piston (radians):", piston)
print("Phase RMSE (radians):", np.sqrt(np.mean(phase_error**2)))
print("Maximum absolute phase error (radians):", np.max(np.abs(phase_error)))
print("Recovered height maximum (m):", height_recovered.max())
print("Height RMSE (m):", np.sqrt(np.mean(height_error**2)))
print("Maximum absolute height error (m):", np.max(np.abs(height_error)))
print("True height PV (m):", height_true.max() - height_true.min())
print("Recovered height PV (m):", height_recovered.max() - height_recovered.min())
print("Height-error PV (m):", height_error.max() - height_error.min())

# 画真实相位，展开并带活塞项，二者误差图
phase_error_frad = phase_error * 1e15
error_limit = np.max(np.abs(phase_error_frad))
fig_phase_recovery, ax_phase_recovery = plt.subplots(1, 3, figsize=(14, 4), layout="constrained")

image_true_phase = ax_phase_recovery[0].imshow(phase_true, cmap="viridis", vmin=phase_true.min(), vmax=phase_true.max(), origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_phase_recovery[0].set_title("True Continuous Phase")

ax_phase_recovery[1].imshow(phase_unwrapped_aligned, cmap="viridis", vmin=phase_true.min(), vmax=phase_true.max(), origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_phase_recovery[1].set_title("Recovered Continuous Phase")

fig_phase_recovery.colorbar(image_true_phase, ax=ax_phase_recovery[:2], label="Phase (radians)")

image_phase_error = ax_phase_recovery[2].imshow(phase_error_frad, cmap="coolwarm", vmin=-error_limit, vmax=error_limit, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_phase_recovery[2].set_title("Phase Error")

fig_phase_recovery.colorbar(image_phase_error, ax=ax_phase_recovery[2], label="Phase error (1e-15 rad)")

# 高度计算并画图
height_true_nm = height_true * 1e9
height_recovered_nm = height_recovered * 1e9
height_error_recovered = height_error * 1e22
error_limit_height = np.max(np.abs(height_error_recovered))

fig_height, ax_height = plt.subplots(1, 3, figsize=(14, 4), layout="constrained")
image_height_real = ax_height[0].imshow(height_true_nm, cmap="viridis", vmin=height_true_nm.min(), vmax=height_true_nm.max(), origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_height[0].set_title("True Height")

ax_height[1].imshow(height_recovered_nm, cmap="viridis", vmin=height_true_nm.min(), vmax=height_true_nm.max(), origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")
ax_height[1].set_title("Recovered Height")

fig_height.colorbar(image_height_real, ax=ax_height[:2], label="height(nm)")

image_height_error = ax_height[2].imshow(height_error_recovered, cmap="coolwarm", vmin=-error_limit_height, vmax=error_limit_height, origin="lower", extent=[x.min(), x.max(), y.min(), y.max()], aspect="equal")

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
case_b_dir = project_root / "results" / "case_b_ideal"
figures_dir = case_b_dir / "figures"
metrics_dir = case_b_dir / "metrics"
metrics_json_path = metrics_dir / "case_b_metrics.json"

figures_dir.mkdir(parents=True, exist_ok=True)
metrics_dir.mkdir(parents=True, exist_ok=True)

fig_intensities.savefig(figures_dir / "01_four_step_intensities.png", dpi=300, bbox_inches="tight")

fig_wrapped_comparison.savefig(figures_dir / "02_wrapped_phase_comparison.png", dpi=300, bbox_inches="tight")

fig_phase_recovery.savefig(figures_dir / "03_continuous_phase_recovery.png", dpi=300, bbox_inches="tight")

fig_height.savefig(figures_dir / "04_height_recovery.png", dpi=300, bbox_inches="tight")
fig_profile.savefig(figures_dir / "05_center_profile.png", dpi=300, bbox_inches="tight")

# 保存相应参数
parameters = {
    "wavelength_m": float(wavelength_m), 
    "background": float(background), 
    "contrast": float(contrast), 
    "height_peak_m": float(height_peak_m)
}
sampling_check = {"max_true_phase_rad": float(phase_true.max()), "max_adjacent_diff_x_rad": float(np.max(np.abs(np.diff(phase_true, axis=1)))), "max_adjacent_diff_y_rad": float(np.max(np.abs(np.diff(phase_true, axis=0)))), "x_sampling_valid": bool(np.max(np.abs(np.diff(phase_true, axis=1))) < np.pi), "y_sampling_valid": bool(np.max(np.abs(np.diff(phase_true, axis=0))) < np.pi)}

wrapped_phase_validation = {"max_circular_error_rad": float(np.max(np.abs(wrapped_error))), "rmse_circular_error_rad": float(np.sqrt(np.mean(wrapped_error**2)))}
direct_wrapped_height_result = {"max_height_m": float(height_from_wrapped_phase.max()), "height_rmse_m": float(np.sqrt(np.mean(height_error_from_wrapped_phase**2))), "max_absolute_height_error_m": float(np.max(np.abs(height_error_from_wrapped_phase)))}

unwrapped_reconstruction = {"piston_rad": float(piston), "phase_rmse_rad": float(np.sqrt(np.mean(phase_error**2))), "max_absolute_phase_error_rad": float(np.max(np.abs(phase_error))), "recovered_height_max_m": float(height_recovered.max()), "height_rmse_m": float(np.sqrt(np.mean(height_error**2))), "max_absolute_height_error_m": float(np.max(np.abs(height_error))), "true_height_pv_m": float(height_true.max() - height_true.min()), "recovered_height_pv_m": float(height_recovered.max() - height_recovered.min()), "height_error_pv_m": float(height_error.max() - height_error.min())}

metrics = {"case_name": "case_b_ideal_static_four_step_psi", "parameters": parameters, "sampling_check": sampling_check, "wrapped_phase_validation": wrapped_phase_validation, "direct_wrapped_height_result": direct_wrapped_height_result, "unwrapped_reconstruction": unwrapped_reconstruction}

with metrics_json_path.open("w", encoding="utf-8") as file:
    json.dump(metrics, file, ensure_ascii=False, indent=2)

plt.show()
