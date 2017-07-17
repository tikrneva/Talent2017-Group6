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

print(number_pos)

# Find only yrast states
Z_yrast = Z_pos[number_pos==1]
A_yrast = A_pos[number_pos==1]
J_yrast = J_pos[number_pos==1]
E_ex_yrast = E_ex_pos[number_pos==1]
parity_yrast = parity_pos[number_pos==1]
number_yrast = number_pos[number_pos==1]

# Find isotopes where 6+ and 8+ yrast states exist 
Z_1 = np.arange(Z_yrast.min(),Z_yrast.max(),2)

Z_86 = []
A_86 = []
E_8 = []
E_6 = []

for i in range(len(Z_1)):
	temp_J = []
	temp_Z = []
	temp_A = []
	temp_E_ex = []
	for j in range(len(Z_yrast)):
		if Z_1[i] == Z_yrast[j]:
			temp_J.append(J_yrast[j])
			temp_Z.append(Z_yrast[j])
			temp_A.append(A_yrast[j])
			temp_E_ex.append(E_ex_yrast[j])	
			if 6 in temp_J and 8 in temp_J:
				# print(Z_1[i])
				# print(temp_J)
				for k in range(len(temp_J)):
					if temp_J[k] == 6:
						Z_86.append(temp_Z[k])
						A_86.append(temp_A[k])
						E_6.append(temp_E_ex[k])
					if temp_J[k] == 8:
						E_8.append(temp_E_ex[k])

Z_86 = np.array(Z_86)
E_8 = np.array(E_8)
E_6 = np.array(E_6)

print(len(Z_86),len(E_8))

plt.plot(Z_86,E_8/E_6,'bo')
plt.show()


# # Find first excited 6 plus states
# Z_6plus = Z_yrast[J_yrast==6]
# A_6plus = A_yrast[J_yrast==6]
# J_6plus = J_yrast[J_yrast==6]
# E_ex_6plus = E_ex_yrast[J_yrast==6]
# parity_6plus = parity_yrast[J_yrast==6]
# number_6plus = parity_yrast[J_yrast==6]

# # Find first excited 8 plus states
# Z_8plus = Z_yrast[J_yrast==8]
# A_8plus = A_yrast[J_yrast==8]
# J_8plus = J_yrast[J_yrast==8]
# E_ex_8plus = E_ex_yrast[J_yrast==8]
# parity_8plus = parity_yrast[J_yrast==8]
# number_8plus = parity_yrast[J_yrast==8]

# Calculate ratio of 8 plus to 6 plus excitation energy
# ratio_8over6 = E_ex_8plus/E_ex_6plus

# plt.plot(Z_8plus,)






