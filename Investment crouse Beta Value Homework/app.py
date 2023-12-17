from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def calculate_beta_and_risk(stock_prices, index_prices):
    stock_returns = np.diff(stock_prices) / stock_prices[:-1]
    index_returns = np.diff(index_prices) / index_prices[:-1]
    covariance = np.cov(stock_returns, index_returns)[0, 1]
    market_variance = np.var(index_returns)
    beta = covariance / market_variance
    total_risk = np.std(stock_returns)
    return beta, total_risk

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    stock_prices = np.array(data['stock'])
    index_prices = np.array(data['twii'])
    beta, total_risk = calculate_beta_and_risk(stock_prices, index_prices)
    return jsonify({'beta': beta, 'total_risk': total_risk})

if __name__ == '__main__':
    app.run(debug=True)
