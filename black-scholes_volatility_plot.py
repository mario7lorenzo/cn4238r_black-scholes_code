import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from BlackScholesModel import BlackScholesModel

def main():
	K = 100
	s = 100
	dt = 1
	r = 0.05
	volatilities = np.arange(0,2,0.01)

	models = [BlackScholesModel(s, K, dt, r, sigma) for sigma in volatilities]
	callPrices = [model.callPrice() for model in models]
	putPrices = [model.putPrice() for model in models]

	plt.plot(volatilities, callPrices, label='Call Options Price')
	plt.plot(volatilities, putPrices, label='Put Options Price')
	plt.xlabel (r'$\sigma$ (Volatility of the underlying asset)')
	plt.ylabel('Options Price')
	plt.title('Volatility vs Options Price')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()