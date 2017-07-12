#============================
# Additional functions 
#=============================

import numpy as np
import matplotlib.pyplot as plt

#==================================================================
# This function permutates array and gives the phase +1 or -1
# depending on the amount of moves in permutation
# RETURNS sign from the permutation and the ordered array
def permutator(array):
    alist = array.tolist()
    nummov=0 #number of moves
    #------------------------------------------------------
    # at first we check that there are no two same elements
    seen = []
    for number in alist:
        if number in seen:
            print "===================================================="
            print "             E R R O R !!!!                     "
            print " Pauli is angry - two particles on the same state!"
            print "===================================================="
            return 0,[]  
        else:
            seen.append(number)
       #The list 'seen' not needed later
    #--------------------------------------------------------
    # PERMUTATOR ITSELF
    #--------------------------------------------------------
    if len(alist)!=0:
       for i in range(0, len(alist)):
           minval=min(alist[i:]) # find min. value between i:th position
                                 # and the last (first i states have already
                                 # been permutated
           minindex=alist.index(minval) # store the index of minval
           nummov=nummov+(minindex-i) #update number of moves needed
           alist.remove(minval) #remove minval from the list
           alist.insert(i,minval) #insert minval in the position i
       ordarray=np.asarray(alist)
       # Even number of moves -> +1, odd number of moves -> -1
       if nummov%2==0:
           sign=1
       else: 
           sign=-1
       return sign,ordarray
    # if len(alist) == 0 then:
    else:
       return 0,array #array is empty

#======================================================================
# LEVEL PLOTTER: plots the given eigenenergies
#======================================================================
def showlevels(energies):
    for e in energies:
        plt.plot((1.0,1.5),(e,e),'k-') #draws a line at energy e
    plt.plot((0.5,2.0),(0,0),'r--')
    plt.ylabel('Energy')
    plt.title('Energy levels')
    plt.xlim([0,2.5])
    plt.tick_params(       # Remove x-tics:
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off
    plt.show()
    return 
