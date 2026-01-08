import matplotlib.pyplot as plt
import numpy as np


def plot_policy_helper(policy, w_space, T, asset_name, cmap):
    fig, ax = plt.subplots(figsize=(10, 5))
    im = ax.imshow(
        policy,
        origin="lower",
        aspect="auto",
        extent=[w_space[0], w_space[-1], 1, T],
        cmap=cmap,
    )
    fig.colorbar(im, ax=ax, label=rf"$u^*({asset_name})$")
    ax.set_xlabel(r"Wealth state $w$")
    ax.set_ylabel(r"Time $t$")
    ax.set_title(f"Optimal Policy Heatmap: {asset_name.upper()} Allocation")
    return fig, ax

def plot_policy_heatmaps(policy_1, policy_2, w_space, T, tickers):
    """
    Create policy heatmaps over (time, wealth).
    """

    n_w = len(w_space)
    times = list(range(1, T + 1))

    # Build P_1, P_2 matrices: rows = time, cols = wealth index
    # policy_1 & policy_2 have rows = wealth index, cols = time
    P_1 = policy_1.T
    P_2 = policy_2.T

    P_risky = P_1 + P_2
    P_cash = 1.0 - P_risky

    figures = {}

    # Asset 0 heatmap
    figures["asset_0"], _ = plot_policy_helper(P_1, w_space, T, tickers[0], "viridis")
    figures["asset_1"], _ = plot_policy_helper(P_2, w_space, T, tickers[1], "plasma")
    figures["risky"], _ = plot_policy_helper(P_risky, w_space, T, "risky", "inferno")
    figures["cash"], _ = plot_policy_helper(P_cash, w_space,  T,"cash", "cividis")

    return figures