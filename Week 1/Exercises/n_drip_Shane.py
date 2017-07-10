# Import packages
import numpy as np
import matplotlib.pyplot as plt
print('')

def BE(N,Z):
	alpha_1, alpha_2, alpha_3, alpha_4 = 15.49, 17.23, 0.697, 22.6
	A = N+Z
	term_1 = alpha_1*A
	term_2 = -alpha_2*A**(2/3)
	term_3 = -alpha_3*(Z**2)*(A**(-1/3))
	term_4 = -alpha_4*((N-Z)**2)/A
	return term_1 + term_2 + term_3 + term_4

Z_temp = np.linspace(36,44,9)
N_temp = np.linspace(50,200,151)

binding_energy = []
Z = []
N = []

for i in range(len(Z_temp)):
	for j in range(len(N_temp)):
		binding_energy.append(BE(N_temp[j],Z_temp[i]))
		Z.append(int(Z_temp[i]))
		N.append(int(N_temp[j]))

Z,N,binding_energy = np.array(Z), np.array(N), np.array(binding_energy)

S_1n = [] 
Z_1 = []
N_1 = []

for i in np.arange(1,len(Z)):
	if Z[i] - Z[i-1] == 0:
		S_1n.append(binding_energy[i]-binding_energy[i-1])
		Z_1.append(Z[i])
		N_1.append(N[i])


S_1n,Z_1,N_1 = np.array(S_1n),np.array(Z_1),np.array(N_1)

Z_36,N_36,S_1n_36 = Z_1[Z_1==36],N_1[Z_1==36],S_1n[Z_1==36]
Z_37,N_37,S_1n_37 = Z_1[Z_1==37],N_1[Z_1==37],S_1n[Z_1==37]
Z_38,N_38,S_1n_38 = Z_1[Z_1==38],N_1[Z_1==38],S_1n[Z_1==38]
Z_39,N_39,S_1n_39 = Z_1[Z_1==39],N_1[Z_1==39],S_1n[Z_1==39]
Z_40,N_40,S_1n_40 = Z_1[Z_1==40],N_1[Z_1==40],S_1n[Z_1==40]
Z_41,N_41,S_1n_41 = Z_1[Z_1==41],N_1[Z_1==41],S_1n[Z_1==41]
Z_42,N_42,S_1n_42 = Z_1[Z_1==42],N_1[Z_1==42],S_1n[Z_1==42]
Z_43,N_43,S_1n_43 = Z_1[Z_1==43],N_1[Z_1==43],S_1n[Z_1==43]
Z_44,N_44,S_1n_44 = Z_1[Z_1==44],N_1[Z_1==44],S_1n[Z_1==44]

N_36_u = N_36[S_1n_36<0]
N_37_u = N_37[S_1n_37<0]
N_38_u = N_38[S_1n_38<0]
N_39_u = N_39[S_1n_39<0]
N_40_u = N_40[S_1n_40<0]
N_41_u = N_41[S_1n_41<0]
N_42_u = N_42[S_1n_42<0]
N_43_u = N_43[S_1n_43<0]
N_44_u = N_44[S_1n_44<0]

print('Predicted neutron dripline with liquid-droplet model')
print('Z=36: N=',N_36_u[0])
print('Z=37: N=',N_37_u[0])
print('Z=38: N=',N_38_u[0])
print('Z=39: N=',N_39_u[0])
print('Z=40: N=',N_40_u[0])
print('Z=41: N=',N_41_u[0])
print('Z=42: N=',N_42_u[0])
print('Z=43: N=',N_43_u[0])
print('Z=44: N=',N_44_u[0])




