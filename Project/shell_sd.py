# Nuclear TALENT 2017
# Tiia, Shane, Martin, Ovidiu
# This code reads the single-particle states and matrix elements of 
# effective interactions for N particles and total angular 
# momentum M and plots the energy eigenvalues

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

# Ask for number of particles N_particles in the system
# (must be less than or equal to number of single-particle states)
N_particles = int(raw_input("Enter number of particles: "))
while ((N_particles > N_sp)):
	print("Wrong input: Number of particles must be less than number of single-particle states", N_sp,". Try again:")
	N_particles = int(raw_input("Enter number of particles: "))

# Ask for total 2*M of the system (Check: if N is even then 2*M should be even, if N is odd then 2*M should be odd)
M_val = int(raw_input("Enter total 2*M of the system: "))
while ((N_particles % 2 != 0) and (M_val % 2 == 0)) or ((N_particles % 2 == 0) and (M_val % 2 != 0)):
	print("Wrong input: if N is even then 2*M should be even, if N is odd then 2*M should be odd. Try again:")
	M_val = int(raw_input("Enter total 2*M-value: "))

# Create all possible Slater determinants
s = range(1,N_sp+1)
sd = find_slaters(s,N_particles)
sd = list(sd)

# Pick the Slater determinants with the given 2*M
sd_m = pickslatersM(sd,m_j,M_val)

# Total number of Slater determinants with 2*M
N_slater = len(sd_m)

# Build Hamiltonian matrix
H = np.zeros((N_slater, N_slater))
for beta in range(0, N_slater):
	# Add single-particle energies to diagonal elements
	H[beta,beta] += diag_element(sd_m[beta],sp_energies,N_particles)
	for a in range(N_me):
		(alpha,phase) = two_body(index1[a],index2[a],index3[a],index4[a],beta,sd_m)
		if phase != 0:
			if alpha == beta:
				H[alpha,beta] += int(phase) * matrix_elements[a]
			else:
				H[alpha,beta] += int(phase) * matrix_elements[a]
				H[beta,alpha] += int(phase) * matrix_elements[a]

# Print Hamiltonian matrix
#print('')
#print("Hamiltonian matrix:")
#for i in range(len(H)):
#	print(H[i])

# Check that the Hamiltonian is symmetric
print('')
print("Hamiltonian is symmetric:")
print((H.transpose() == H).all())

# Diagonalize the Hamiltonian matrix
print('')
print("Energy eigenvalues:")
w,v = LA.eig(H)
print(sorted(w))

# Plot the energies
showlevels(w)