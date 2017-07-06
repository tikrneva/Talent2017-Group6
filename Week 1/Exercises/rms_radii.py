import numpy as np
import matplotlib.pyplot as plt
from uncertainties import * 
from uncertainties import unumpy as u
print('')

# Load data
radii_data = np.loadtxt('rms13.dat',skiprows=2,usecols=[0,1,2,3,4])


# Assign variables of each isotopes to lists and convert to arrays

Z = []
A = []
N = []
radii = []
radii_error = []

for i in range(len(radii_data)):
	Z.append(int(radii_data[i,0]))
	N.append(int(radii_data[i,1]))
	A.append(int(radii_data[i,2]))
	radii.append(radii_data[i,3])
	radii_error.append(radii_data[1,4])

Z = np.array(Z)
A = np.array(A)
N = np.array(N)
radii = np.array(radii)
radii_error = np.array(radii_error)

# Order list in ascending Z

Z_i = np.arange(Z.min(),Z.max()+0.1,1)

Z_1 = []
N_1 = []
A_1 = []
radii_1 = []
radii_error_1 = []

for i in range(len(Z_i)):
	for j in range(len(Z)):
		if Z[j] == Z_i[i]:
			N_1.append(N[j])
			Z_1.append(Z[j])
			A_1.append(A[j])
			radii_1.append(radii[j])
			radii_error_1.append(radii_error[j])

# makes uncertainties uarray of radii and their errors

radii_1 = u.uarray(radii_1,radii_error_1)

# Calcualte rms(N) - rms(N-1) (checking that elements differ by only 1 neutron number)

radiinn1 = []
Nnn1 = []
Znn1 = []

for i in np.arange(1,len(Z_1)-1,1):
	if Z_1[i] == Z_1[i-1]:
		if N_1[i] == N_1[i-1] + 1:
			radiinn1.append(radii_1[i]-radii_1[i-1])
			Nnn1.append(N_1[i])
			Znn1.append(Z_1[i])

radiinn1 = np.array(radiinn1)
Nnn1 = np.array(Nnn1)
Znn1 = np.array(Znn1)

# Plot either with errorbars or without

# plt.errorbar(Nnn1,u.nominal_values(radiinn1),yerr=u.std_devs(radiinn1),fmt='bo',markersize=0,label='All')
plt.plot(Nnn1,u.nominal_values(radiinn1),'bo',label='All')

# Plot mercury data in different colour
NHg = Nnn1[Znn1==80]
radiiHg = radiinn1[Znn1==80]
# plt.errorbar(NHg,u.nominal_values(radiiHg),yerr=u.std_devs(radiiHg),fmt='ro',markersize=0,label='Hg')
plt.plot(NHg,u.nominal_values(radiiHg),'ro',label='$_{80}$Hg')

# Plot yttrium data in different colour
NY = Nnn1[Znn1==39]
radiiY = radiinn1[Znn1==39]
# plt.errorbar(NBe,u.nominal_values(radiiBe),yerr=u.std_devs(radiiBe),fmt='go',markersize=0,label='Be')
plt.plot(NY,u.nominal_values(radiiY),'go',label='$_{39}$Y')

plt.xlabel('Neutron number')
plt.ylabel(r'$\delta \sqrt{\langle r^{2} \rangle}^{N,N-1}}$ (fm)')

# Plot with limits on y to show shell structure
plt.ylim(-0.08,0.15)
plt.savefig('rmsdata_zoom.pdf',bbox_inches='tight')

# plt.savefig('rmsdata.pdf',bbox_inches='tight')

plt.legend()
plt.show()