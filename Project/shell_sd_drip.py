# Nuclear TALENT 2017
# Tiia, Shane, Martin, Ovidiu
# This code reads the single-particle states and effective interactions 
# for oxygen isotopes N=[2,4,6,8,12] and total angular momentum 
# M=0 and plots the neutron separation energies

import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy
import matplotlib.pyplot as plt
from numpy import linalg as LA
import itertools
from add_funcs import pickpairs,showlevels,find_slaters,diag_element,pickslatersM,two_body

# Load single-particle data from file 'sdshellint.dat' ordered as (index, n, l, 2j, 2m_j)
sp_data = np.loadtxt('spdata_sd.dat',skiprows=2,usecols=[0,1,2,3,4,5])

index = []
n = []
l = []
j = []
m_j = []
sp_energies = []

for i in range(len(sp_data)):
	index.append(int(sp_data[i,0]))
	n.append(int(sp_data[i,1]))
	l.append(int(sp_data[i,2]))
	j.append(int(sp_data[i,3]))
	m_j.append(int(sp_data[i,4]))
	sp_energies.append(sp_data[i,5])

index = np.array(index)
n = np.array(n)
l = np.array(l)
j = np.array(j)
m_j = np.array(m_j)
sp_energies = np.array(sp_energies)

# Load effective interactions from file 'shellint_sd.dat' ordered as (i,j,k,l,<ij|V|kl>
int_data = np.loadtxt('shellint_sd.dat',skiprows=2,usecols=[0,1,2,3,4])

index1 = []
index2 = []
index3 = []
index4 = []
matrix_elements = []

for i in range(len(int_data)):
	index1.append(int(int_data[i,0]))
	index2.append(int(int_data[i,1]))
	index3.append(int(int_data[i,2]))
	index4.append(int(int_data[i,3]))
	matrix_elements.append(int_data[i,4])

index1 = np.array(index1)
index2 = np.array(index2)
index3 = np.array(index3)
index4 = np.array(index4)
matrix_elements = np.array(matrix_elements)

# Number of single-particle states
N_sp = len(index)

# Number of matrix elements of effective interaction
N_me = len(matrix_elements)

# Array with even oxygen isotopes
N_arr = np.linspace(2,12,6)

# Set total M to zero
M_val = 0

be = []
levels = []

# Loop over the even oxygen isotopes
for N_particles in range(2,12,2):

	# Create all possible Slater determinants
	s = range(1,N_sp+1)
	sd = find_slaters(s,N_particles)
	sd = list(sd)
	
	# Pick the Slater determinants with the given 2*M
	sd_m = pickslatersM(sd,m_j,M_val)
	
	# Total number of Slater determinants with 2*M
	N_slater = len(sd_m)
	
	#print(matrix_elements)
	
	# Include scaling factor
	scaling_factor = (18/(16+float(N_particles)))**0.3
	matrix_elements = scaling_factor * matrix_elements
	
	# Build Hamiltonian matrix
	H = np.zeros((N_slater, N_slater))
	for beta in range(0, N_slater):
		# Add single-particle energies to diagonal elements
		H[beta,beta] = H[beta,beta] + diag_element(sd_m[beta],sp_energies,N_particles)
		for a in range(N_me):
			(alpha,phase) = two_body(index1[a],index2[a],index3[a],index4[a],beta,sd_m)
			if phase != 0:
				if alpha == beta:
					H[alpha,beta] += int(phase) * matrix_elements[a]
				else:
					H[alpha,beta] = H[alpha,beta] + int(phase) * matrix_elements[a]
					H[beta,alpha] = H[beta,alpha] + int(phase) * matrix_elements[a]
		
	# Diagonalize the Hamiltonian matrix
	w,v = LA.eig(H)
	
	# Set ground state to zero
	lowest = w.min()
	w0 = w - lowest

	# Choose levels below 6 MeV
	w0 = w0[w0<6]

	# Save levels and binding energy
	be.append(lowest)
	levels.append(w0)
	
# Plot the levels
#showlevels(levels)

# Calculate neutron seperation energy to find drip point
s2n = []
ns2n = []
N_part = np.linspace(2,12,6)

for i in range(1,len(be)):
	s2n.append(abs(be[i])-abs(be[i-1]))
	ns2n.append(N_part[i]+16)

plt.plot(ns2n,s2n,'bo')
plt.ylabel('Neutron separation energy')
plt.xlabel('N')
plt.show()
