import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from BlackScholesModel import BlackScholesModel

def main():
	K = 100
	s = 100
	r = 0.05
	sigma = 0.2
	timeToMaturities = np.arange(0,2,0.01)

	models = [BlackScholesModel(s, K, dt, r, sigma) for dt in timeToMaturities]
	callPrices = [model.callPrice() for model in models]
	putPrices = [model.putPrice() for model in models]

	plt.plot(timeToMaturities, callPrices, label='Call Options Price')
	plt.plot(timeToMaturities, putPrices, label='Put Options Price')
	plt.xlabel ('dt (Time to Maturity, in years)')
	plt.ylabel('Options Price')
	plt.title('Time to Maturity vs Options Price')
	plt.legend()
	plt.show()
	return

if __name__ == '__main__':
	main()