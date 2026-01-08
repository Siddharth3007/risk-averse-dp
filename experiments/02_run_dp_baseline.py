from radp.config.settings import *
from radp.dp.solver import solve_dp
import pandas as pd
import json
import numpy as np
import copy


cfg_dict = {"Tickers": tickers, "Horizon": T, "Sample Size": n_samples, "Terminal Penalty": k, \
            "Risk Free Rate (Daily)": rf, "Target Return Rate (Daily)": r_target, \
            "Risk Aversion Parameter": lmbda, "CVaR Tail Loss Severity": alpha, \
            "Wealth Grid Step Size": w_step, "Wealth Grid Max": w_max, "Wealth Grid Min": w_min, \
            "Control Grid Step Size": u_step, "Control Grid Max": u_max, "Control Grid Min": u_min, \
            "Wealth Update Method": wealth_update_method}


rets = pd.read_excel("./data/processed/rets_{0}_{1}_{2}.xlsx".format(tickers[0], tickers[1], historical_period))
policy_1, policy_2, V, w_space, u_space, ret_samples = solve_dp(cfg_dict, rets)

# Saving Metadata
metadata = copy.deepcopy(cfg_dict)

with open("results/metadata/baseline_run.json", "w") as f:
    json.dump(metadata, f, indent=2)

# Saving numerical arrays
np.savez(
    "results/arrays/baseline_run.npz",
    policy_1=policy_1.values,
    policy_2=policy_2.values,
    V=V.values,
    w_space=w_space,
    u_space=u_space
)




