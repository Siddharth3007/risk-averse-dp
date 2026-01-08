import numpy as np

def make_wealth_grid(w_min, w_max, w_step):
    w_space = np.arange(w_min, w_max + w_step, w_step)
    return w_space

def round_wealth(w, w_space, w_step):
    w_min = w_space[0]
    w_idx = (w - w_min)/w_step
    w_idx = np.round(w_idx).astype(int)
    w_idx = np.clip(w_idx, 0, len(w_space) - 1)
    return w_idx

def make_control_grid(u_min, u_max, u_step):
    u_space_1d = np.arange(u_min, u_max + u_step, u_step)
    u_space = []

    for u_1 in u_space_1d:
        for u_2 in u_space_1d:
            if u_1 + u_2 <= 1: # u1, u2 >= 0; u1 + u2 <= 1 implies no shorting & no leverage
                u_space.append([u_1, u_2])

    u_space = np.array(u_space)  # n_controls x n_assets
    return u_space

