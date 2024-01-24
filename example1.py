import numpy as np
import pandas as pd

import sph_harm

# Import the model for CFy

CFy_model = pd.read_csv('CFy.csv', index_col = None)

orders  = CFy_model['order'].to_list()
degrees = CFy_model['degree'].to_list()
betas   = CFy_model['beta'].to_list()

# Sample a sweep of constant alpha'

alpha_primes = np.ones(30) * (np.pi/2)
phi_primes = np.linspace(0, np.pi, 30)

CFy_sample = 0

for i in range(len(betas)):

    y_lm = sph_harm.basis_fn(degrees[i], orders[i], alpha_primes, phi_primes)
    CFy_sample += betas[i] * y_lm

print("="*40)
print("{:^40}".format("CFy Sample"))
print("="*40)
print("{:^10} {:^12} {:^12}".format("polar [deg]", "azim [deg]", "CFy"))

for i in range(len(CFy_sample)):
    print("     {:<10} {:<10} {:<10}".format(
                                    np.round(np.degrees(alpha_primes[i]), 1), 
                                    np.round(np.degrees(phi_primes[i]), 1), 
                                    np.round(CFy_sample[i], 3)))
print("="*40)