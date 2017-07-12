# Nuclear TALENT 2017
# Tiia, Shane, Martin
# This code compute the energy eigenvalues for no-broken pairs

import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Load single-particle data from file 'sp.dat' ordered as (index, n, l, 2j, 2m_j)
sp_data = np.loadtxt('sp.dat',skiprows=2,usecols=[0,1,2,3,4])
index = []
n = []
l = []
j = []
m_j = []

for i in range(len(sp_data)):
	index.append(int(sp_data[i,0]))
	n.append(int(sp_data[i,1]))
	l.append(int(sp_data[i,2]))
	j.append(int(sp_data[i,3]))
	m_j.append(int(sp_data[1,4]))

index = np.array(index)
n = np.array(n)
l = np.array(l)
j = np.array(j)
m_j = np.array(m_j)

# Number of single-particle states
N_sp = len(index)

# Ask for number of particles N_particles in the system
N_particles = int(raw_input("Enter number of particles: "))
while ((N_particles > N_sp) or (N_particles % 2!=0)):
	print("Wrong input: Number of particles must even and less than number of single-particle states", N_sp,". Try again:")
	N_particles = int(raw_input("Enter number of particles: "))

# Construct all Slater determinants (e.g. to get state of particle 3 in first Slater determinant: sd[0,2])
# TODO: Need to generalize to arbitrary number of particles
sd = []
for i in range(1, N_sp-2):
	for j in range(i+1, N_sp-1):
		for k in range(j+1, N_sp):
			for l in range(k+1, N_sp+1):
				if j == i+1 and l == k+1 and i % 2==1 and k % 2 ==1:
					sd.append([i,j,k,l])

# Turn it into an array
sd = np.array(sd)

# Total number of Slater determinants
N_slater = len(sd)

# Function that takes two-body operator indices p,q,r,s and index alpha for the ket Slater determinant 
# and returns the index beta of the new Slater determinant
def two_body(p,q,r,s,alpha):
	if (r in sd[alpha]) and (s in sd[alpha]) and (p != q) and (r !=s) and (p not in sd[alpha]) and (q not in sd[alpha]):
		# Replace the r- and s-values in alpha with p and q.
		slater = copy.deepcopy(sd[alpha])
		slater2 = slater 
		slater2[slater.tolist().index(s)] = q
		slater2[slater.tolist().index(r)] = p
		slater2.sort()
		beta = sd.tolist().index(slater2.tolist())
		return beta
	elif (r in sd[alpha]) and (s in sd[alpha]) and (p != q) and (r !=s) and (p == r) and (q == s):
		return alpha
	else:
		# new Slater determinant is zero (set index to -1)
		beta = -1
		return beta

# Function that calculates diagonal element in the Hamiltonian for Slater determinant alpha
def one_body(alpha):
	slater = copy.deepcopy(sd[alpha])
	value = 2*(int(slater[1]/2)-1)+2*(int(slater[3]/2)-1)
	return value

# Two-body matrix element
g = 1
V = -g

# Build Hamiltonian matrix
H = np.zeros((N_slater, N_slater))
for alpha in range(0, N_slater):
	for beta in range(0, N_slater):
		if alpha==beta:
			# Diagonal elements
			H[alpha,beta] = one_body(alpha)
		for p in range(1, N_sp+1):
			for q in range(1, N_sp+1):
				for r in range(1, N_sp+1):
					for s in range(1, N_sp+1):
						if ((p==1 and q==2) or (p==3 and q==4) or (p==5 and q==6) or (p==7 and q==8)) and ((r==1 and s==2) or (r==3 and s==4) or (r==5 and s==6) or (r==7 and s==8)):
							gamma = two_body(p,q,r,s,alpha)
							if beta == gamma:
								H[alpha,beta] += V

# Print Hamiltonian matrix
print('')
print("Hamiltonian matrix:")
for i in range(len(H)):			
	print(H[i])

# Diagonalize the Hamiltonian matrix
print('')
print("Energy eigenvalues:")
w,v = LA.eig(H)
print w

# Plot energies (if you are testing program, comment this so 
# you don't get a figure every single time when running a program)
showlevels(np.array(w)) #"showlevels" is in add_funcs.py
