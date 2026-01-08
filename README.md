# Risk-Averse Dynamic Programming for Portfolio Allocation

## Overview
This project implements a **risk-averse multi-period portfolio optimization problem**
using **dynamic programming with a nested Mean–CVaR risk measure**.

The goal is to study how optimal portfolio policies change when downside risk
is accounted for *dynamically* over time, rather than using a single-period risk
penalty.

The current implementation serves as a **baseline research framework**, designed
to be modular, reproducible, and extensible.

---

## Methodology
- The portfolio problem is formulated as a **finite-horizon Markov Decision Process (MDP)**.
- Wealth evolves according to a discrete-time stochastic wealth dynamics model.
- At each time step, the investor chooses portfolio weights subject to budget constraints.
- Risk is modeled using a **nested Mean–CVaR dynamic risk measure**, ensuring time consistency.
- Future uncertainty is handled via **scenario generation** (baseline: historical bootstrap).

Key components:
- State: current wealth (discretized on a grid)
- Action: portfolio allocation across risky assets and cash
- Objective: minimize dynamic risk of terminal shortfall relative to a target

---

## Project Structure
src/radp/
├── dp/              # Dynamic programming logic (grid, Bellman recursion, solver)
├── risk/            # Risk measures (Mean, CVaR, Mean–CVaR)
├── models/          # Wealth dynamics
├── scenarios/       # Scenario generation (historical bootstrap)
├── plotting/        # Reusable plotting utilities
└── config/          # Configuration defaults

experiments/
├── 01_make_dataset.py        # Data download & preprocessing
├── 02_run_dp_baseline.py     # Baseline DP run
└── 03_plot_policy_baseline.py# Visualization of results

data/
└── processed/       # Processed return data

results/
├── metadata/        # JSON metadata describing each run
├── arrays/          # Numerical outputs (policies, value functions, grids)
└── figures/         # Generated plots


---

## How to Run

### 1. Create dataset

python experiments/01_make_dataset.py'''


### 2. Run baseline DP

python experiments/02_run_dp_baseline.py

### 3. Plot Results
python experiments/03_plot_policy_baseline.py

## Outputs
The baseline pipeline produces:
- Optimal portfolio policies as a function of wealth and time
- Policy heatmaps for individual assets, total risky allocation, and cash

Results are saved in:
- results/arrays/ (NumPy .npz files)
- results/metadata/ (JSON configuration)
- ults/figures/ (PNG plots)

