import numpy as np

def oil_own_rate_log(spot_price, future_price, r, T_days):
    """
    spot_price: spot price of oil
    future_price: future price of oil
    r: real interest rate
    T_days: time to maturity in days
    """
    T = T_days / 365
    return r + (1/T) * np.log(spot_price/future_price)