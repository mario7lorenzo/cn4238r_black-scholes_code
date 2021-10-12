from scipy.stats import norm
import numpy as np

'''
This is the Black-Scholes model defined in the Object-Oriented Programming style.

Input Parameters:
s: Spot price of the underlying asset
K: Strike price
dt: Time to maturity or expiration date
r: Risk-free interest rate
sigma: The volatility of the underlying asset

Author: Mario Lorenzo
'''

class BlackScholesModel:
	def __init__(self, s, K, dt, r, sigma):
		self.s = s
		self.K = K
		self.dt = dt
		self.r = r
		self.sigma = sigma
		self.d1 = (np.log(self.s / self.K) + (self.r + self.sigma**2/2) * self.dt) / (self.sigma * np.sqrt(self.dt))
		self.d2 = self.d1 - self.sigma*np.sqrt(self.dt)

	def callPrice(self):
		return self.s* norm.cdf(self.d1) - self.K* np.exp(-self.r*self.dt)* norm.cdf(self.d2)

	def putPrice(self):
		return self.K*np.exp(-self.r*self.dt)*norm.cdf(-self.d2) - self.s*norm.cdf(-self.d1)


