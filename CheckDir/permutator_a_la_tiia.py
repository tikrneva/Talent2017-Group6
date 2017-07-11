#============================
# Permutator a la Tiia
#=============================

import numpy as np

# This function permutates array and gives the phase +1 or -1
# depending on the amount of moves in permutation
# TODO: this does NOT check if there are two same values in the array?
def permutator(array):
    alist = array.tolist()
    nummov=0 #number of moves
    if len(alist)!=0:
       for i in range(0, len(alist)):
           minval=min(alist[i:]) #find min. value between i:th position
                                 # and the last (first i states have already
                                 # been permutated
           minindex=alist.index(minval)
           nummov=nummov+(minindex-i) #update number of moves needed
           alist.remove(minval) #remove minval from the list
           alist.insert(i,minval) #insert minval in the position i
       ordarray=np.asarray(alist)
       if nummov%2==0:
           sign=1
       else: 
           sign=-1
       return sign,ordarray
    else:
       return 0,array #array is empty

# Just testing, these can be removed =============>
myarr1 = np.array([1,3,4,5])
myorderedarray = np.array([1,3,4,5])
testsign, testarray = permutator(myarr1)
print testsign, testarray
