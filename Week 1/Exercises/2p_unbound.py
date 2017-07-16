# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import uncertainties
from uncertainties import unumpy
print('')

# Load data from file
mass_data = np.loadtxt('aud16.dat',skiprows=2)

# Create empty lists to read data into
Z = []
A = []
BE = []
BE_error = []
N = []

# Assign variables of a given isotope to each list
for i in range(len(mass_data)):
	Z.append(int(mass_data[i,0]))
	A.append(int(mass_data[i,1]))
	BE.append(mass_data[i,2])
	BE_error.append(mass_data[i,3])
	N.append(int(mass_data[i,5]))

# Assign variables of a given isotope to each list
Z = np.array(Z)
A = np.array(A)
BE = np.array(BE)
BE_error = np.array(BE_error)
BE = unumpy.uarray(BE,BE_error)
N = np.array(N)

# Create array of each Z and N in arrays
Z_i = np.arange(Z.min(),Z.max()+0.1,1)
N_i = np.arange(N.min(),N.max()+0.1,1)

# Create empty lists for reordering
N_1 = []
Z_1 = []
BE_1 = []

# Reorder lists into isotones of given N number
for i in range(len(N_i)):
	for j in range(len(N)):
		if N[j] == N_i[i]:
			N_1.append(N[j])
			Z_1.append(Z[j])
			BE_1.append(BE[j])

# Create empty lists for S_2p
S_2p = []
S_1p = []
N_S_2p= []
Z_S_2p = []

# Calculate and add S_2p, S_1p (and Z,N) for isotones for which it can be computed
for i in np.arange(2,len(N_1)-1,1):
	if N_1[i] == N_1[i-2]:
		S_2p.append(BE_1[i]-BE_1[i-2])
		S_1p.append(BE_1[i]-BE_1[i-1])
		N_S_2p.append(N_1[i])
		Z_S_2p.append(Z_1[i])

# Turn them into arrays
S_2p = np.array(S_2p)
S_1p = np.array(S_1p)
N_S_2p = np.array(N_S_2p)
Z_S_2p = np.array(Z_S_2p)

# Find which isotopes are unbound to 2 proton decay
S_2p_u = S_2p[S_2p < 0]
S_1p_2p_u = S_1p[S_2p < 0]
N_S_2p_u = N_S_2p[S_2p < 0]
Z_S_2p_u = Z_S_2p[S_2p < 0]

# Find which of these isotopes are unbound to 2 proton decay but stable to 1 proton decay
print('These isotopes are unbound to two proton decay:')
print('N 	 Z 	 S2p 		 S1p')
for i in range(len(N_S_2p_u)):
	print(Z_S_2p_u[i],'	',N_S_2p_u[i]+Z_S_2p_u[i],'	',S_2p_u[i],'	',S_1p_2p_u[i])
print('')

N_1p_b_2p_u = N_S_2p_u[S_1p_2p_u > 0]
Z_1p_b_2p_u = Z_S_2p_u[S_1p_2p_u > 0]
S_2p_u = S_2p_u[S_1p_2p_u > 0]
S_1p_b_2p_u = S_1p_2p_u[S_1p_2p_u > 0]

print('These isotopes are unbound to proton decay but stable to one proton decay')
print('Z 	 N 	 S2p 		 S1p')
for i in range(len(N_1p_b_2p_u)):
	print(Z_1p_b_2p_u[i],'	',N_1p_b_2p_u[i]+Z_1p_b_2p_u[i],'	',S_2p_u[i],'	',S_1p_b_2p_u[i])


# # Create empty lists for reordering
# N_1 = []
# Z_1 = []
# BE_1 = []

# # Reorder lists into isotones of given Z number
# for i in range(len(Z_i)):
# 	for j in range(len(Z)):
# 		if Z[j] == Z_i[i]:
# 			N_1.append(N[j])
# 			Z_1.append(Z[j])
# 			BE_1.append(BE[j])


# # Create empty lists for S_2n
# S_2n = []
# S_1n = []
# N_S_2n= []
# Z_S_2n = []

# # Calculate and add S_2p, S_1p (and Z,N) for isotones for which it can be computed
# for i in np.arange(1,len(Z_1)-1,1):
# 	if Z_1[i] == Z_1[i-2]:
# 		S_2n.append(BE_1[i]-BE_1[i-2])
# 		S_1n.append(BE_1[i]-BE_1[i-1])
# 		N_S_2n.append(N_1[i])
# 		Z_S_2n.append(Z_1[i])

# S_2n = np.array(S_2n)
# N_S_2n = np.array(N_S_2n)
# Z_S_2n = np.array(Z_S_2n)

# S_2n = S_2n[Z_S_2n==8]
# N_S_2n = N_S_2n[Z_S_2n==8]
# S_2n /= 1000

# plt.errorbar(N_S_2n,unumpy.nominal_values(S_2n),yerr=unumpy.std_devs(S_2n),fmt='bo')
# plt.xlabel('Neutron number')
# plt.ylabel('$S_{2n}$ (M8V)')
# plt.xlim(5,19)
# plt.ylim(-1,50)
# plt.savefig('S_2n_even_N.pdf',bbox_inches='tight')
# plt.show()

