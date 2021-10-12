import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from BlackScholesModel import BlackScholesModel

def main():
	K = 100
	r = 0.05
	dt = 1
	sigma = 0.2

	S = np.arange(60,160,0.1)
	models = [BlackScholesModel(s, K, dt, r, sigma) for s in S]
	callPrices = [model.callPrice() for model in models]
	putPrices = [model.putPrice() for model in models]

	plt.plot(S, callPrices, label='Call Options Price')
	plt.plot(S, putPrices, label='Put Options Price')
	plt.xlabel ('s (Spot Price of the Underlying Asset)')
	plt.ylabel('Options Price')
	plt.title('Spot Price vs Options Price')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()