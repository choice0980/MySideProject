import numpy as np

def stock_beta_and_totalRisk(stock_closing_prices, twii_closing_prices):
    # 任意股票XXXXX (XXXXX.TW) 的收盤價數據 , 加權指數 (^TWII) 的收盤價數據

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
    total_risk = np.std(stock_returns)

    print('This sotck\'s Beta: ', beta, '\nThis stock\'s total risk: ', total_risk)

