# SHELL MODEL PROJECT 

## Files:
easymain.py : This file includes the very first test version. Basically, test cases "2 levels, 2 pairs" and "4 levels, 2 pairs" have been implemented in such a way that Hamiltonians have been calculated by hand and written explicitly in the code. 

add_funcs.py : This file includes additional functions which are used or have been used in the project. This file includes functions as:
   permutator: permutates the occupied states into the increasing order and gives the phase (+1 or -1) which comes from the number of made permutations (even -> +1, odd -> -1)
   levelplotter: just plots given eigenvalues 
   pickpairs: picks the slater determinants which fulfill the pairing condition (this is only for the very first problem, where we have always only two particles on the same level)
   pickpairsljm: picks the slater determinants which fulfill the pairing condition (n,l and j must be same)
   pickslatersM: picks the slater determinants which have a given total M
      
sp.dat : the file includes single particle states and the related indexing for the 4 level case (only two particles at the same level)

No_broken.py : the main program for the ''no broken pairs'' case. It does the following:
   It loads the single particle state information from a file and saves them into the variables n,l,j and m
   It asks how many particles you want to have in your system
   It calculates all possible slater determinants
   It picks those slater determinants which are relevant for the studied problem
   It calculates two-body matrix element by using the picked slater determinants
   It calculates diagonal elements (one-body part)
   It builds the Hamiltonian 
   It diagonalizes Hamiltonian (calculates eigenenergies)
   It prints and plots eigenenergies
