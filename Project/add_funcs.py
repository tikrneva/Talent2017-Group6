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


#==============================================================================================
# Routine that picks only those slater
# determinants of the pairing problem
#
# E.g. with input:
#
# myslaters=[[1,2,3,4],[1,2,4,5],[3,4,5,8],[1,2,7,8],[3,5,6,7], [3,4,5,6], [3,4,7,8], [1,6,7,8]]
#
# you will get
#
# [[1, 2, 3, 4], [1, 2, 7, 8], [3, 4, 5, 6], [3, 4, 7, 8]]
#==============================================================================================
def pickpairs(allslaters):
   notsuitable = np.zeros(len(allslaters)) #this is just an array for marking 0=fine, 1=not suitable sd
   for sd in allslaters:
      sdind=allslaters.index(sd) #index for the slater determinant which is studied now
      if len(sd)%2 != 0:         # check that there are even number of particles now
         print "Number of particles is not even!" 
         return []
      halflen=len(sd)/2         # I want to loop over 2*i so I have to take a half of the upper limit
      for i in range(0,halflen):
          if sd[2*i]%2 == 0:    # First, third... particle must be on an odd state 
             notsuitable[sdind]=1
          elif sd[2*i+1]%2 !=0: # Second, fourth... particle must be on an even state
             notsuitable[sdind]=1
          elif sd[2*i] != sd[2*i+1]-1: # Because we have pairs and sd's are ordered, 1st and 2nd particle must be 1,2 or 3,4 etc
             notsuitable[sdind]=1
   suitableslaters = []
   for ind in range(0,len(notsuitable)):
       if (notsuitable[ind] == 0):
          suitableslaters.append(allslaters[ind]) # finally we combine suitable slater determinants
   return suitableslaters
