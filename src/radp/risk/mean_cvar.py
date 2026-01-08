import numpy as np

def cvar(costs, alpha): # CVaR helper
    var = np.quantile(costs, alpha, axis = 1).reshape(costs.shape[0], 1)
    mask = costs >= var # Right Tail Mask
    tail_sm = np.sum(costs*mask, axis = 1)
    tail_ct = np.sum(mask, axis = 1)
    return tail_sm/np.maximum(tail_ct, 1)

def mean(costs): # Expectation helper
    return np.mean(costs, axis = 1)

def compute_mean_cvar(costs, lmbda, alpha): # One-step Conditional Risk (Mean-CVaR)
    e = mean(costs)
    cv = cvar(costs, alpha)
    return (1 - lmbda)*e + lmbda*cv