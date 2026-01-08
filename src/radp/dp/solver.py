import pandas as pd
from radp.dp.grid import make_wealth_grid, make_control_grid, round_wealth
from radp.scenarios.generator import historical_bootstrap
from radp.models.wealth_dynamics import update_wealth
from radp.dp.bellman import recursion


def solve_dp(cfg, rets):
    tickers = cfg["Tickers"]
    T = cfg["Horizon"]
    n_samples = cfg["Sample Size"]
    k = cfg["Terminal Penalty"]
    rf = cfg["Risk Free Rate (Daily)"]
    lmbda = cfg["Risk Aversion Parameter"]
    alpha = cfg["CVaR Tail Loss Severity"]
    r_target = cfg["Target Return Rate (Daily)"]
    w_step = cfg["Wealth Grid Step Size"]
    w_max = cfg["Wealth Grid Max"]
    w_min = cfg["Wealth Grid Min"]
    u_step = cfg["Control Grid Step Size"]
    u_max = cfg["Control Grid Max"]
    u_min = cfg["Control Grid Min"]
    method = cfg["Wealth Update Method"]
    w_target = 1 * (1 + r_target * T)

    # Forming Wealth Grid
    w_space = make_wealth_grid(w_min, w_max, w_step)

    # Forming Control Grid
    u_space = make_control_grid(u_min, u_max, u_step) # n_controls x n_assets

    # Generating Return Samples
    ret_samples = historical_bootstrap(rets[tickers], n_samples)  # n_samples x n_assets

    V = pd.DataFrame()
    policy_1 = pd.DataFrame()
    policy_2 = pd.DataFrame()

    for w_idx in range(len(w_space)):
        w = w_space[w_idx]
        V.loc[w_idx, T + 1] = k * max(w_target - w, 0)

    for i in range(T, 0, -1):
        print(i)

        for w_idx in range(len(w_space)):
            w = w_space[w_idx]
            w_next = update_wealth(w, ret_samples, u_space, rf, method = method) # n_controls x n_samples

            stage_cost = -1 * (w_next - w)

            w_next_idx = round_wealth(w_next, w_space, w_step)
            w_next_idx = w_next_idx.flatten()
            cont_val = V.loc[w_next_idx, i + 1].values  # Continuation Value (V_{t+1})
            cont_val = cont_val.reshape(u_space.shape[0], n_samples)

            # Bellman's Recursive Update Step (finding best control/action)
            u_best_idx, vt_min = recursion(stage_cost, cont_val, lmbda, alpha)  # n_controls x 1
            V.loc[w_idx, i] = vt_min
            policy_1.loc[w_idx, i] = u_space[u_best_idx, 0]
            policy_2.loc[w_idx, i] = u_space[u_best_idx, 1]


    return policy_1, policy_2, V, w_space, u_space, ret_samples