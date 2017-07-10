# Import packages
import numpy as np
import matplotlib.pyplot as plt
print('')

# Define constants (in MeV) for binding energies in Liquid-drop model without pairing term (from Alex's notes)
a1 = 15.49
a2 = 17.23
a3 = 0.697
a4 = 22.6

# Create arrays for N and Z
N_arr = []
Z_arr = range(36,44)

# Compute drip-line points N for each Z by looping of over N until the neutron seperation energy becomes negative
for Z in range(36, 44):
	N = Z
	N1 = N-1
	A = Z+N
	A1 = Z+N1
	BE0 = a1*A-a2*(A**(2/3))-a3*(Z**2)/(A**(1/3))-a4*((N-Z)**2)/A
	BE1 = a1*A1-a2*(A1**(2/3))-a3*(Z**2)/(A1**(1/3))-a4*((N1-Z)**2)/A1
	while ((BE0-BE1)>0):
		N = N+1
		N1 = N-1
		A = Z+N
		A1 = Z+N1	
		BE0 = a1*A-a2*(A**(2/3))-a3*(Z**2)/(A**(1/3))-a4*((N-Z)**2)/A
		BE1 = a1*A1-a2*(A1**(2/3))-a3*(Z**2)/(A1**(1/3))-a4*((N1-Z)**2)/A1
	N_arr.append(N)

# Plot neutron drip-line
plt.plot(N_arr,Z_arr)
plt.ylabel('Z')
plt.xlabel('N')
plt.title('Neutron drip-line with Liquid-drop model')
plt.axis([92, 113, 35, 45])
plt.show()
