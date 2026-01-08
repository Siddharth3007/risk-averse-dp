import numpy as np

def update_wealth(w, r, u, rf, method = "linear"):
    '''
    Calculates wealth for next step
    :param w: Current Wealth
    :param r: Return Samples (n_samples x n_assets)
    :param u: Control/Action Space (n_controls x n_assets)
    :param rf: Daily Risk Free Rate
    :param method: "linear" or "exp"
    :return: Next Step Wealth
    '''
    u_cash = 1 - np.sum(u, axis = 1) # Assuming no leverage, u_cash >= 0
    u_cash = u_cash.reshape(-1, 1)

    if method == "linear":
        w_next = w*(u_cash*(1+rf) + u @ ((1+r).T))  # n_controls x n_samples
    elif method == "exp":
        w_next = w * (u_cash * np.exp(rf) + u @ ((np.exp(r)).T))  # n_controls x n_samples

    return w_next
