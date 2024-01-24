import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sph_harm

# Import the model for CFy

CFy_model = pd.read_csv('CFy.csv', index_col = None)

orders  = CFy_model['order'].to_list()
degrees = CFy_model['degree'].to_list()
betas   = CFy_model['beta'].to_list()

# Plot the entire surface

alpha_primes = np.linspace(0, np.pi, 30)
phi_primes = np.linspace(-np.pi, np.pi, 60)
alpha_primes, phi_primes = np.meshgrid(alpha_primes, phi_primes)

CFy_sample = 0

for i in range(len(betas)):
    y_lm = sph_harm.basis_fn(degrees[i], orders[i], alpha_primes, phi_primes)
    CFy_sample += betas[i] * y_lm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('alpha prime [deg]')
ax.set_ylabel('phi prime [deg]')
ax.set_zlabel('CFy')
ax.plot_wireframe(np.degrees(alpha_primes), np.degrees(phi_primes), CFy_sample,
                                                                    color='0.2')
plt.show()