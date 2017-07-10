#============================================
# NUCLEAR TALENT 2017
# Shell model project by
# Martin, Shane and Tiia
#
#===========================================

import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy import *


# 4 particle - 4 level Hamiltonian (for tests?)
def pair_H(g):
    return np.array([[2-2*g, -g,-g,-g,-g,0], \
                     [-g,4-2*g,-g,-g,0,-g],  \
                     [-g,-g,6-2*g,0,-g,-g],  \
                     [-g,-g,0,6-2*g,-g,-g],  \
                     [-g,0,-g,-g,8-2*g,-g],  \
                     [0,-g,-g,-g,-g,10-2*g]])


# This diagonalizes a given matrix
def diagonalize_matrix(yourmat):
    eigvals, eigvecs = LA.eig(yourmat) # LA.eig gives eigenvalues and eigenvectors of the matrix  
    return eigvals, eigvecs


# Plotting
gs = np.linspace(-1.0, 1.0, 100)
for i in gs:
   H_i = pair_H(i)
   evals, evecs = diagonalize_matrix(H_i)
   ivals=[i,i,i,i,i,i]
   plt.plot(ivals,evals, 'ro')
plt.xlabel('g')
plt.ylabel('Eigenvalue')
plt.title('Pairing Hamiltonian eigenvalues as a function of g')
plt.show()
