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

# Simple Hamiltonian for tests
def simple_H(g):
    return np.array([[-g,-g],[-g, 2-g]])

# 4 particle - 4 level Hamiltonian (for tests?)
def pair_H(g):
    return np.array([[2-2*g, -g,-g,-g,-g,0], \
                     [-g,4-2*g,-g,-g,0,-g],  \
                     [-g,-g,6-2*g,0,-g,-g],  \
                     [-g,-g,0,6-2*g,-g,-g],  \
                     [-g,0,-g,-g,8-2*g,-g],  \
                     [0,-g,-g,-g,-g,10-2*g]])

# If we need symbolic diagonalization, these lines do it:
#g = Symbol('g')
#M = Matrix([[-g,-g],[-g, 2-g]])
#print ("Symbolic eigenvalues: ")
#print M.eigenvals()

# This diagonalizes a given matrix
def diagonalize_matrix(yourmat):
    eigvals, eigvecs = LA.eig(yourmat) # LA.eig gives eigenvalues and eigenvectors of the matrix  
    #TODO return also diagonal representation of matrix?
    return eigvals, eigvecs


# Some tests 
# TODO: remove these
print ("Hamiltonian matrix g=1")
H1=simple_H(1)
print H1
w,v = LA.eig(H1)
print w
evals, evecs = diagonalize_matrix(H1)
Hpair=pair_H(1)
print Hpair
