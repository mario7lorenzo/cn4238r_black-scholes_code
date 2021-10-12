import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from BlackScholesModel import BlackScholesModel

def main():
	K = 100
	s = 100
	dt = 1
	sigma = 0.2
	rates = np.arange(0,1,0.01)

	models = [BlackScholesModel(s, K, dt, r, sigma) for r in rates]
	callPrices = [model.callPrice() for model in models]
	putPrices = [model.putPrice() for model in models]

	plt.plot(rates, callPrices, label='Call Options Price')
	plt.plot(rates, putPrices, label='Put Options Price')
	plt.xlabel ('r (Risk-free Interest Rate)')
	plt.ylabel('Options Price')
	plt.title('Risk-Free Interest Rate vs Options Price')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()