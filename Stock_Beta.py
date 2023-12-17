import numpy as np


# 加權指數 (^TWII) 的收盤價數據
twii_closing_prices = np.array([17483.99, 17418.34, 17450.63, 17468.93, 17653.11])

# 任意股票XXXXX (XXXXX.TW) 的收盤價數據
stock_closing_prices = np.array([35.42, 35.47, 35.58, 36.06, 36.55])

# 計算日收益率
twii_returns = np.diff(twii_closing_prices) / twii_closing_prices[:-1]
stock_returns = np.diff(stock_closing_prices) / stock_closing_prices[:-1]

# 計算平均收益率
mean_twii_returns = np.mean(twii_returns)
mean_stock_returns = np.mean(stock_returns)

# 計算協方差和市場變異數
covariance = np.cov(stock_returns, twii_returns)[0, 1]
market_variance = np.var(twii_returns)

# 計算 Beta 值
beta = covariance / market_variance
beta

print('This sotck\'sBeta: ', beta)

