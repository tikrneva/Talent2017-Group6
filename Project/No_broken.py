# Nuclear TALENT 2017
# Tiia, Shane, Martin, Ovidiu
# This code compute the energy eigenvalues for no-broken pairs

import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy
import matplotlib.pyplot as plt
from numpy import linalg as LA
import itertools
from add_funcs import pickpairs,showlevels

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

# Functions that returns a set of set of possible Slater determinant for set of states s and m number of particles
def find_slaters(s,m):
	return set(itertools.combinations(s,m))

# Create all possible Slater determinants
s = range(1,N_sp+1)
sd = find_slaters(s,N_particles)

# Create all Slater determinants with no broken pairs
sd = list(sd)
sd_pairs = pickpairs(sd)
sd_pairs_temp = []

for i in range(len(sd_pairs)):
	sd_pairs_temp.append(list(sd_pairs[i]))

# Total number of Slater determinants
N_slater = len(sd_pairs_temp)

# Function that takes two-body operator indices p,q,r,s and index alpha for the ket Slater determinant 
# and returns the index beta of the new Slater determinant
def two_body(p,q,r,s,alpha,sd_pairs2):
	if (r in sd_pairs2[alpha]) and (s in sd_pairs2[alpha]) and (p != q) and (r !=s) and (p not in sd_pairs2[alpha]) and (q not in sd_pairs2[alpha]):
		# Replace the r- and s-values in alpha with p and q.
		slater = list(copy.deepcopy(sd_pairs2[alpha]))
		sd_pairs2 = list(sd_pairs2)
		slater2 = slater 
		slater2[slater.index(s)] = q
		slater2[slater.index(r)] = p
		slater2.sort()
		beta = sd_pairs2.index(slater2)
		return beta
	elif (r in sd_pairs2[alpha]) and (s in sd_pairs2[alpha]) and (p != q) and (r !=s) and (p == r) and (q == s):
		return alpha
	else:
		# new Slater determinant is zero (set index to -1)
		beta = -1
		return beta

# Function that calculates diagonal element in the Hamiltonian for Slater determinant alpha
def one_body(alpha,sd_pairs2):
	slater = copy.deepcopy(sd_pairs2[alpha])
	value = 0
	for i in range(1,N_particles,2):
		value += 2*(int(slater[i]/2)-1)
		#value = 2*(int(slater[1]/2)-1)+2*(int(slater[3]/2)-1)
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
			H[alpha,beta] = one_body(alpha,sd_pairs_temp)
		for p in range(1, N_sp+1):
			for q in range(1, N_sp+1):
				for r in range(1, N_sp+1):
					for s in range(1, N_sp+1):
						if ((p==1 and q==2) or (p==3 and q==4) or (p==5 and q==6) or (p==7 and q==8)) and ((r==1 and s==2) or (r==3 and s==4) or (r==5 and s==6) or (r==7 and s==8)):
							gamma = two_body(p,q,r,s,alpha,sd_pairs_temp)
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

# Plot the energies
showlevels(w)
