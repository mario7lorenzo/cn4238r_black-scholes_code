import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.stats import norm
from BlackScholesModel import BlackScholesModel

def main():
	s = 60
	dt = 1
	sigma = 0.2
	r = 0.05
	strikePrices = np.arange(0, 100, 1)


	models = [BlackScholesModel(s, K, dt, r, sigma) for K in strikePrices]
	callPrices = [model.callPrice() for model in models]
	putPrices = [model.putPrice() for model in models]


	plt.plot(strikePrices, callPrices, label='Call Options Price')
	plt.plot(strikePrices, putPrices, label='Put Options Price')
	plt.xlabel ('K (Strike Price)')
	plt.ylabel('Options Price')
	plt.title('Strike Price vs Options Price')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()