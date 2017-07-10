# Nuclear TALENT 2017
# Tiia, Shane, Martin

import numpy as np
import matplotlib.pyplot as plt

# Load single-particle data from file 'sp.dat' ordered as (index, n, l, 2j, 2m_j)
sp_data = np.loadtxt('sp.dat',skiprows=2,usecols=[0,1,2,3,4])
index = []
n = []
l = []
j = []
m_j = []

N_sp = len(index)

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

# Ask for total M (store as 2*M) of the system and number of particles N
N_particles = raw_input("Enter number of particles: ")
M_val = raw_input("Enter total 2*M-value: ")
N_particles=int(N_particles)
M_val=int(M_val)

# (Check: if N is even then 2*M should be even, if N is odd then 2*M should be odd)
while ((N_particles % 2 != 0) and (M_val % 2 == 0)) or ((N_particles % 2 == 0) and (M_val % 2 != 0)):
	print("Wrong input: if N is even then 2*M should be even, if N is odd then 2*M should be odd. Try again:")
	N_particles = raw_input("Enter number of particles: ")
	M_val = raw_input("Enter total 2*M-value: ")
	N_particles=int(N_particles)
	M_val=int(M_val)

# Construct all Slater determinants and store the total M-value for each Slater determinant
sd = []
M = []
for i in range(1, N_sp-3):
	for j in range(i+1, N_sp-2):
		for k in range(j+1, N_sp-1):
			for l in range(k+1, N_sp):
				sd.append = [i,j,k,l]
				M.append = m_j[i]+m_j[j]+m_j[k]+m_j[l]

# Takes two-body operator indices p,q,r,s and index alpha for the ket Slater determinant and returns the index beta of the new Slater determinant (as well as phase for broken-pair case)
#def printme(p,q,r,s,alpha):
#	if r =! alpha(1) or r != alpha(2) or r != alpha(3) or r != alpha(4) or s =! alpha(1) or s != alpha(2) or s != alpha(3) or s != alpha(4)
#	beta = 0
#	else
#	# Replace the r- and s-values in alpha with p and q.		
#   return beta
