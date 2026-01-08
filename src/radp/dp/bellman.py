from radp.risk.mean_cvar import compute_mean_cvar
import numpy as np

def recursion(stage_cost, cont_val, lmbda, alpha):
    ''' Performs one step backward recursion for a given state and time
    stage_cost: Current Stage cost (n_controls x n_samples)
    cont_val: Contrinuation Value/ Next Step value function (n_controls x n_samples)'''
    vt = compute_mean_cvar(stage_cost + cont_val, lmbda, alpha)  # n_controls x 1
    u_best_idx = np.argmin(vt)
    vt_min = vt[u_best_idx]
    return u_best_idx, vt_min