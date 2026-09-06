# Python Simulation

This directory contains the Python implementation for the ideal static four-step phase-shifting interferometry simulation.

## Run

From this directory, run:

```powershell
python -m scripts.simulate_static_four_step
```

## Current scope

Case B uses an 800 nm Gaussian reflective surface at a wavelength of 632.8 nm. The workflow is:

```text
true height -> true phase -> four interferograms -> wrapped phase
-> sequential unwrapping -> piston alignment -> recovered height
```

The script saves figures and scalar metrics under `results/case_b_ideal/`.

## Structure

```text
src/       Reusable surface and phase-processing functions
scripts/   Runnable simulation scripts
results/   Generated figures and JSON metrics
```

The current unwrapping method applies one-dimensional `numpy.unwrap` sequentially along the two axes. It is suitable for the smooth, noise-free case here and is not a general two-dimensional unwrapping algorithm.
