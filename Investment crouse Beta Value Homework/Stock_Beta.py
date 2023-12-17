import numpy as np

def stock_beta_and_totalRisk(stock_closing_prices, index_closing_prices):

    # 計算日收益率
    index_returns = np.diff(index_closing_prices) / index_closing_prices[:-1]
    stock_returns = np.diff(stock_closing_prices) / stock_closing_prices[:-1]

    # 計算共變異數和市場變異數
    covariance = np.cov(stock_returns, index_returns)[0, 1]
    market_variance = np.var(index_returns)

    # 計算 Beta 值
    beta = covariance / market_variance
    total_risk = np.std(stock_returns)

    print('This sotck\'s Beta: ', beta, '\nThis stock\'s total risk: ', total_risk)

stock_price = np.array([10, 11, 12, 13, 14])
index_price = np.array([100, 110, 120, 130, 140])
stock_beta_and_totalRisk(stock_price,index_price )

