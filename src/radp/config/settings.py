# General Parameters
T = 10
tickers = ['^GSPC', 'TLT']
historical_period = "10y"
wealth_update_method = "linear" # {"linear", "exp"}

# Rates given below are per-day (annualized rate / 252)
rf = 0.04/252
r_target = 0.2/252

# Cost parameters
k = 100 # Terminal Penalty

# Scenario Generation Parameters
n_samples = 5000
gen_method = "empirical" # {"empirical", "normal", "student-t"}

# Risk Parameters
lmbda = 0.025 # Risk Aversion Parameter
alpha = 0.95

# Wealth Grid Parameters
w_max = 2
w_min = 0
w_step = 0.005

# Control Grid Parameters
u_max = 1
u_min = 0
u_step = 0.05