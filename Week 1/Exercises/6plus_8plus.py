import numpy as np
import matplotlib.pyplot as plt
from uncertainties import * 
from uncertainties import unumpy as u
print('')

# Load data
ToIEE_data = np.loadtxt('toiee.dat',skiprows=1,usecols=[1,2,3,4,5,6])

# Assign variables of each isotopes to lists and convert to arrays
Z = []
A = []
J = []
parity = []
number = []
E_ex = []

for i in range(len(ToIEE_data)):
	A.append(int(ToIEE_data[i,0]))
	Z.append(int(ToIEE_data[i,1]))
	J.append(int(ToIEE_data[i,2]))
	parity.append(int(ToIEE_data[i,3]))
	number.append(int(ToIEE_data[i,4]))
	E_ex.append(ToIEE_data[i,5])

Z = np.array(Z)
A = np.array(A)
J = np.array(J)
parity = np.array(parity)
number = np.array(number)
E_ex = np.array(E_ex)

# Find only positive parity states 
Z_pos = Z[parity==1]
A_pos = A[parity==1]
J_pos = J[parity==1]
E_ex_pos = E_ex[parity==1]
parity_pos = parity[parity==1]
number_pos = number[parity==1]

# Find only yrast states
Z_yrast = Z_pos[number_pos==1]
A_yrast = A_pos[number_pos==1]
J_yrast = J_pos[number_pos==1]
E_ex_yrast = E_ex_pos[number_pos==1]
parity_yrast = parity_pos[number_pos==1]
number_yrast = number_pos[number_pos==1]

# Find J=6
Z_y6=[]
A_y6=[]
J_y6=[]
E_ex_y6=[]
for i in range(0,len(J_yrast)):
    if J_yrast[i]==6:
       Z_y6.append(Z_yrast[i])
       A_y6.append(A_yrast[i])
       J_y6.append(J_yrast[i])
       E_ex_y6.append(E_ex_yrast[i])

# Find J=8
Z_y8=[]
A_y8=[]
J_y8=[]
E_ex_y8=[]
for i in range(0,len(J_yrast)):
    if J_yrast[i]==8:
       Z_y8.append(Z_yrast[i])
       A_y8.append(A_yrast[i])
       J_y8.append(J_yrast[i])
       E_ex_y8.append(E_ex_yrast[i])

#Calculate ratios
ratios86=[]
finalZ=[]
finalA=[]
finalN=[]
for i in range(0,len(Z_y6)):
    for j in range(0, len(Z_y8)):
       if Z_y8[j] == Z_y6[i] and A_y8[j] == A_y6[i]:
          ratios86.append(E_ex_y8[j]/E_ex_y6[i])
          finalZ.append(Z_y6[i])
          finalA.append(A_y6[i])
          finalN.append(A_y6[i]-Z_y6[i])

#Plot
plt.plot(finalN,ratios86, 'ro')
plt.xlabel('N')
plt.ylabel('E(8)/E(6)')
plt.title('Ratio of the 8+ to 6+ energies for yrast states')
plt.ylim(0.5,2.5)
plt.show()
           
