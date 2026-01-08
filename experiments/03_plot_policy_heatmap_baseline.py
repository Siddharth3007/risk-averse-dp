import matplotlib.pyplot as plt
import numpy as np
from radp.plotting.policy_plots import plot_policy_heatmaps
import json

# Loading policy and wealth grid
array_data = np.load("results/arrays/baseline_run.npz")
policy_1 = array_data["policy_1"]
policy_2 = array_data["policy_2"]
w_space = array_data["w_space"]

print(policy_1.shape)

# Loading Metadata
with open("results/metadata/baseline_run.json", "r") as f:
    cfg = json.load(f)
T = cfg["Horizon"]
tickers = cfg["Tickers"]

figs = plot_policy_heatmaps(policy_1, policy_2, w_space, T, tickers)

figs["asset_0"].savefig("results/figures/policy_asset0_heatmap.png", dpi=300, bbox_inches="tight")
figs["asset_1"].savefig("results/figures/policy_asset1_heatmap.png", dpi=300, bbox_inches="tight")
figs["risky"].savefig("results/figures/policy_risky_heatmap.png", dpi=300, bbox_inches="tight")
figs["cash"].savefig("results/figures/policy_cash_heatmap.png", dpi=300, bbox_inches="tight")

plt.show()