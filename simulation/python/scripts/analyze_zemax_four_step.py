"""Read four unnormalized Zemax detector exports and recover wrapped phase.

Requires NumPy and Pillow. File row order is preserved; no claim about the
physical sign of the detector Y axis is made. Original project decoder reused.
"""
from pathlib import Path
import argparse
import colorsys
import hashlib
import json
import shutil
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'simulation/python/src'))
from phase_processing import decode_wrapped_phase


def read_export(path):
    lines = path.read_text(encoding='utf-16').splitlines()
    rows = []
    for line in lines:
        fields = line.split()
        if len(fields) == 257 and fields[0].isdigit():
            row = int(fields[0])
            if row == len(rows) + 1:
                rows.append([float(v) for v in fields[1:]])
    data = np.asarray(rows)
    assert data.shape == (256, 256), (path, data.shape)
    assert np.isfinite(data).all() and (data >= 0).all()
    assert '相干辐照度' in '\n'.join(lines[:24])
    return data, '\n'.join(lines[:23])


FONT = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'


def label(draw, xy, text, size=22, fill='#182433'):
    draw.text(xy, text, font=ImageFont.truetype(FONT, size), fill=fill)


def map_panel(canvas, xy, data, size, vmax=None, phase_mask=None):
    if phase_mask is None:
        gray = (255 * (1 - np.clip(data / vmax, 0, 1))).astype('uint8')
        rgb = np.repeat(gray[:, :, None], 3, axis=2)
    else:
        lut = np.array([colorsys.hsv_to_rgb(i / 255, .82, .93)
                        for i in range(256)]) * 255
        ids = np.clip((data + np.pi) / (2*np.pi) * 255, 0, 255).astype(int)
        rgb = lut[ids].astype('uint8')
        rgb[~phase_mask] = (231, 234, 238)
    canvas.paste(Image.fromarray(rgb).resize((size, size)), xy)
    draw = ImageDraw.Draw(canvas)
    x, y = xy
    draw.rectangle((x, y, x+size, y+size), outline='#8a96a5', width=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--inputs', type=Path, default=ROOT /
                    'simulation/python/results/zemax_four_step_2026-10-26/inputs')
    ap.add_argument('--output', type=Path, default=ROOT /
                    'simulation/python/results/zemax_four_step_2026-10-26')
    args = ap.parse_args()
    out = args.output
    (out / 'inputs').mkdir(parents=True, exist_ok=True)
    arrays, provenance = [], {}
    for name in ['I0', 'I90', 'I180', 'I270']:
        p = args.inputs / (name + '.txt')
        data, header = read_export(p)
        arrays.append(data)
        provenance[name] = dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                                header=header, minimum=float(data.min()),
                                maximum=float(data.max()))
        if p.resolve() != (out / 'inputs' / p.name).resolve():
            shutil.copy2(p, out / 'inputs' / p.name)
    i0, i90, i180, i270 = arrays
    background = sum(arrays) / 4
    amplitude = np.hypot(i0-i180, i270-i90) / 2
    modulation = amplitude / np.maximum(background, 1e-30)
    phase = decode_wrapped_phase(*arrays)
    mask = (background > .15*background.max()) & (modulation > .25)
    # This mask is an analysis choice, not an instrument acceptance criterion.
    coordinate = (np.arange(256)+.5)*10/256-5
    strip = np.array([a[:, 96:160].mean(axis=1) for a in arrays])
    strip /= background[:, 96:160].mean(axis=1)
    selected = abs(coordinate) < 3
    def fit(frequency):
        t = 2*np.pi*frequency*coordinate[selected]
        design = np.column_stack((np.ones(t.size), np.cos(t), np.sin(t)))
        coeff = np.linalg.lstsq(design, strip[:, selected].T, rcond=None)[0]
        residual = design @ coeff - strip[:, selected].T
        return float(np.mean(residual**2)), coeff
    # Bounded golden-section fit of common spatial frequency, independent of theory.
    lo, hi = .9, 1.3
    ratio = (np.sqrt(5)-1)/2
    for _ in range(70):
        left, right = hi-ratio*(hi-lo), lo+ratio*(hi-lo)
        if fit(left)[0] < fit(right)[0]:
            hi = right
        else:
            lo = left
    frequency = (lo+hi)/2
    _, coeff = fit(frequency)
    fitted_phase = np.unwrap(np.arctan2(-coeff[2], coeff[1]))
    relative_deg = np.degrees(fitted_phase-fitted_phase[0])
    closure = (i0+i180)-(i90+i270)
    closure_ratio = np.sqrt(np.mean(closure[mask]**2)) / np.sqrt(
        np.mean(((i0+i180+i90+i270)/2)[mask]**2))
    pitch_theory = .0006328 / np.sin(np.deg2rad(.04))
    # Circular residual against fixed theoretical carrier, with ONE fitted offset.
    reference = -2*np.pi*coordinate[:, None]/pitch_theory
    offset = np.angle(np.sum(amplitude[mask] * np.exp(1j*(phase-reference)[mask])))
    residual = np.angle(np.exp(1j*(phase-reference-offset)))
    # Unwrap only a connected, illuminated segment of the central column.
    center = 127
    start, stop = 128, 128
    while start > 0 and mask[start-1, center]:
        start -= 1
    while stop < 256 and mask[stop, center]:
        stop += 1
    profile = np.unwrap(phase[start:stop, center])
    row_ids = np.arange(start, stop)+1
    ideal_profile = reference[start:stop, 0]+offset
    ideal_profile += 2*np.pi*np.round(np.median((profile-ideal_profile)/(2*np.pi)))
    metrics = dict(shape=[256, 256], detector_width_mm=10,
        source_wavelength_nm_assumed=632.8, pixel_pitch_mm=10/256,
        input_provenance=provenance, fit_period_mm=1/frequency,
        theoretical_period_mm=float(pitch_theory),
        fitted_relative_steps_deg=relative_deg.tolist(),
        sign_convention='Increasing file row index, positive spatial carrier in intensity fit; physical Y orientation not verified.',
        mask_background_fraction=.15, mask_modulation_minimum=.25,
        valid_pixels=int(mask.sum()), mask_fraction=float(mask.mean()),
        median_modulation=float(np.median(modulation[mask])),
        pair_sum_relative_rms=float(closure_ratio),
        theoretical_carrier_circular_residual_rms_rad=float(np.sqrt(np.mean(residual[mask]**2))),
        limitations=['No absolute phase accuracy or surface height ground truth.',
                     'Sequentially acquired frames, not simultaneous polarization channels.',
                     'No independent per-frame intensity normalization applied.',
                     'Exports alone do not certify ray trace completion or detector coherent-power normalization settings.'])
    (out/'metrics.json').write_text(json.dumps(metrics, indent=2, ensure_ascii=False))
    np.savez_compressed(out/'phase_results.npz', **dict(zip(['I0','I90','I180','I270'],arrays)),
        background=background, amplitude=amplitude, modulation=modulation,
        wrapped_phase_rad=phase, valid_mask=mask, pair_sum_residual=closure,
        theoretical_carrier_residual_rad=residual,
        central_profile_rows=row_ids, central_unwrapped_phase_rad=profile)

    canvas = Image.new('RGB', (1280, 495), 'white')
    draw = ImageDraw.Draw(canvas)
    label(draw, (30, 14), 'Zemax 四帧原始相干辐照度（同一灰度范围）', 30)
    vmax = max(a.max() for a in arrays)
    for j, (name, data) in enumerate(zip(['I0','I90','I180','I270'],arrays)):
        x = 35+315*j
        label(draw, (x, 65), name, 26)
        map_panel(canvas, (x, 105), data, 265, vmax=vmax)
        label(draw, (x, 385), f'相对拟合相位 {relative_deg[j]:.2f}°', 20)
    label(draw, (35, 433), f'白色 = 0；黑色 = {vmax:.3f} W/cm²。每幅 256 × 256 像素；保持文件行列顺序。', 21)
    canvas.save(out/'01_four_frames.png')

    canvas = Image.new('RGB', (1280, 680), 'white')
    draw = ImageDraw.Draw(canvas)
    label(draw, (30, 14), '从干涉强度恢复包裹相位（Wrapped Phase）', 30)
    label(draw, (60, 74), '相位图：灰色区域不参与分析', 24)
    map_panel(canvas, (60, 120), phase, 410, phase_mask=mask)
    label(draw, (60, 542), '横向：文件列号；纵向：文件行号递增 ↓', 18)
    # Phase colorbar with a cyclic scale; no invented physical Y orientation.
    for k in range(410):
        color=tuple(int(255*v) for v in colorsys.hsv_to_rgb(k/409,.82,.93))
        draw.line((60+k, 580, 60+k, 600), fill=color)
    label(draw, (60, 605), '−π', 20)
    label(draw, (260, 605), '0', 20)
    label(draw, (443, 605), '+π', 20)
    label(draw, (600, 74), '中心列：仅展开连续有效区内的相位', 23)
    box=(620,130,1210,515)
    xmin,xmax=float(row_ids.min()),float(row_ids.max())
    ymin=float(min(profile.min(),ideal_profile.min()))-1
    ymax=float(max(profile.max(),ideal_profile.max()))+1
    def point(x,y):
        return (box[0]+(x-xmin)/(xmax-xmin)*(box[2]-box[0]),
                box[3]-(y-ymin)/(ymax-ymin)*(box[3]-box[1]))
    for value in np.linspace(ymin,ymax,5):
        yy=point(xmin,value)[1]
        draw.line((box[0],yy,box[2],yy),fill='#dce2e8')
        label(draw, (563,yy-12), f'{value:.0f}',18)
    for value in np.linspace(xmin,xmax,5):
        xx=point(value,ymin)[0]
        draw.line((xx,box[1],xx,box[3]),fill='#edf0f3')
        label(draw,(xx-16,box[3]+8),f'{value:.0f}',18)
    draw.rectangle(box,outline='#7f8a98')
    draw.line([point(x,y) for x,y in zip(row_ids,ideal_profile)],fill='#e09327',width=5)
    draw.line([point(x,y) for x,y in zip(row_ids,profile)],fill='#2166ac',width=2)
    label(draw,(620,100),'相位 / rad',18)
    label(draw,(835,550),'文件行号',20)
    label(draw,(620,590),'蓝：四帧恢复值',20, '#2166ac')
    label(draw,(860,590),'橙：理论斜率 + 拟合常数',20, '#b77417')
    label(draw,(620,630),f'条纹周期：拟合 {1/frequency:.4f} mm；理论 {pitch_theory:.4f} mm',21)
    canvas.save(out/'02_phase_recovery.png')

    readme=f'''# Zemax 四步相移数据分析（2026-10-26）

使用用户提供的 I0、I90、I180、I270 原始文本；每幅 256×256，探测器 10×10 mm，相干辐照度单位 W/cm²。原文件副本和 SHA256 已保留。输入未再次分别归一化。

## 方法和结果

- 复用原项目 `simulation/python/src/phase_processing.py` 的解码器：φ = atan2(I270−I90, I0−I180)。φ 的范围为 −π 到 π。
- 四帧共用载频拟合的相对相位：{', '.join(f'{v:.3f}°' for v in relative_deg)}。
- 相位符号依赖约定：上述拟合使用文件行号递增、强度载频取正的约定。不能据此独立判定物理 Y 方向或反射镜运动正负。文件名表示计划施加的相移标签，不是实测相位符号。
- 条纹周期拟合：{1/frequency:.6f} mm；理论值：{pitch_theory:.6f} mm（假定 λ=632.8 nm，镜面附加倾斜 0.02°）。
- 分析区域：四帧平均背景 > 峰值的15%，且调制度 > 0.25；共 {int(mask.sum())} 像素，占全图 {mask.mean():.2%}。阈值为本次分析选择。
- 区域内调制度中位数 {np.median(modulation[mask]):.4f}。
- 相反相位帧和的相对 RMS 差 {closure_ratio:.2%}，即检验 (I0+I180) 与 (I90+I270) 的一致程度；不是相位误差百分比。
- 固定理论载频、只拟合一个常数后的圆周相位残差 RMS {np.sqrt(np.mean(residual[mask]**2)):.5f} rad。它只描述所选区域与理想倾斜模型的偏离，不能解释为测量精度。

## 图像与物理意义

`01_four_frames.png` 使用统一灰度，显示移动反射镜改变相位后条纹平移。`02_phase_recovery.png` 左图显示包裹相位：颜色跳变来自相位以2π为周期表示；右图仅沿连续有效的中心列展开，可见倾斜波前的近似线性相位。

这一步完成从 Zemax 强度数据到相位数据的连接。当前是依次移动镜面取得四幅图；尚不是 Novak/Millerd 的同步偏振四通道，也没有证明动态测量或真实面形精度。文本文件本身不能核实每次追迹是否无错误完成，或相干功率归一化设置；这些应在后续模型记录中保留。探测器局部 Y 与文本行序方向尚未核对，图中明确使用文件行列号。

## 重现

需 NumPy 和 Pillow。从项目根目录运行 `python simulation/python/scripts/analyze_zemax_four_step.py`，默认使用本结果目录中保存的 `inputs/` 四份文本，并输出到 `simulation/python/results/zemax_four_step_2026-10-26/`。可用 `--inputs <输入目录>` 和 `--output <结果目录>` 指定其他位置。主要数组在 `phase_results.npz`，详细统计与原始头信息在 `metrics.json`。
'''
    (out/'README.md').write_text(readme)
    # Check the existing decoder's sign convention against known synthetic phases.
    known=np.linspace(-3,3,101)
    synthetic=[2+np.cos(known+k*np.pi/2) for k in range(4)]
    assert np.max(abs(np.angle(np.exp(1j*(decode_wrapped_phase(*synthetic)-known))))) < 1e-12
    print(json.dumps({k:v for k,v in metrics.items() if k != 'input_provenance'},indent=2,ensure_ascii=False))
    print('Output:',out)


if __name__ == '__main__':
    main()
