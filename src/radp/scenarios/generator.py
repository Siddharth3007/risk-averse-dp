import numpy as np

def historical_bootstrap(rets, n_samples):
    '''Historical Bootstrapping Simulation while preserving cross-asset correlation
    rets: Pandas DataFrame, rows = time points, columns = assets'''
    x = np.random.randint(len(rets), size = n_samples)
    ret_samples = rets.iloc[x, :].values # n_samples x n_assets
    return ret_samples