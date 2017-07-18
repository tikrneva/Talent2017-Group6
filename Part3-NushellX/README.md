# PART 3: NUSHELLX CALCULATIONS

### Task 1: Test your effective interaction and setup of single-particle energies by computing the spectra of 18O and 18F (USDA and USDB, compare to experiments)
This is just a NushellX run for two different nuclei and two different interaction. Two spectra are shown in the  following figures (the other two are similar).

![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/oxygen_isotopes/18Ospectrum.png)

![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/F_isotops/18F_usdb.png)

### Task 2: Perform shell-model studies using Nushellx for all oxygen isotopes from 18O to 28O, plot the lowest-lying 3-4 states and compare with data where available
All oxygen isotopes from 18O to 28O are calculated and the level plots (in .eps format) can be found in the directory ![oxygen_isotopes](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/oxygen_isotopes). Also the excitation energy of the first 2 plus state for even-N oxygen isotopes is plotted.

### Task 3: Perform also shell-model studies using Nushellx for all isotopes from 18F to 29F, plot the lowest-lying 3-4 states and compare with data where available. Comment your results. Try also to compute 30F and 31F
The isotopes from 18F to 29F have been calculated and the level plots can be found in the directory ![F_isotops](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/F_isotops). 

Also 30F and 31F were calculated, the levels can be found in the following figures. 

![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/f_30m.png)
![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Part3-NushellX/f_31m.png)

How to calculate 30F in nushellx? You can take 16O as a core. That means you will have 1 valence proton and 13 valence neutrons.
The goal: you want to study this system in the way that you have 1 valence proton in sd shell and 1 valence neutron in pf shell.
Like always, create a folder, e.g. "f30" (inside nushellx directory) and move into it on a command line. Then type ''shell'' 
and answer the questions in the following way.

 - name for batch file: f30
 - option: lpe
 - model space: sdpf
 - any restrictions: y
 - (s)ub-shell restrictions: m                  [Comment: m=you want to use major shells differently]
 - number of proton major shells, max 2J: 2     [Comment: you have sd and pf =2 major shells]
 - number of orbits, min, max in group 1: 3, 1, 1   [Comment: you have 3 orbits is sd shell (s1/2, d5/2 and d3/2), 1proton]
 - number of orbits, min, max in group 2: 4,0,0   [You assume that one proton stays in sd shell so now 0 protons, in pf shell you have 4 orbits]
 - number of proton major shells, max 2J: 2
 - number of orbits, min, max in group 1: 3, 12, 12 [sd shell full of neutrons]
 - number of orbits, min, max in group 2: 4,1,1 [one neutron in pf shell]
 - interaction name: sdpfmu
 - number of protons: 9
 - number of nucleons: 30
 - min J, max J, del J : 0.0,6.0,1
 - parity: 2                                  [Comment: 1 would be enough]
 - option (lpe, den, help or st) :st
 
 and then type ". f30.bat"


### Task 4: See also if you can find excited states in 25O and 25F with negative parity

### Task 5: Use the monopole interactions to calculate the energies for the ground states of the four nuclei 22−25O assuming a single Slater determinant for each. The USDB two-body matrix elements are assumed to scale like 18/A^0.3.

### Task 6: Compare the results in the last problem to the full 1s0d model space results and to experiment

### Task 7: Calculate the spectroscopic factors from the ground state of 23O to all states in 22O in the full 1s0d model space. Use the sum rule to obtain the orbital occupations in 23O for 0d5/2,1s1/2 and 0d3/2. Compare these to those given in the so-called xxx.occ file

### Task 8: Calculate the spectroscopic factors from the ground state of 23Oto all states in 24O in the full 1s0d model space. Use the sum rule to obtain the number of holes in those three orbits in 23O. Compare these to those given in the xxx.occ file.

### Task 9: Calculate the 23O 5/2(+,1) to 22O 0(+,1) spectroscopic factor. Explain why it is so small.
Added all files for Task 9 in /Task 9/o23_n_decay
The most important file is called o23nb.lsf which is in /Task 9/
Also added the .ans files so people can see what needs to be input into Nushellx to calculate this.

### Task 10: Use the interaction wspot to obtain the single-particle decay width for the 23O 5/2 (+,1) state using the experimental neutron separation energy as a constraint. Combine this with the result of the last problem to obtain its neutron decay width. Compare to experiment.

### Task 11: Calculate the neutron decay width of the 25O 3/2(+,1) state and compare to experiment.  Use the experimental neutron separation energy as a constraint.
Shane, Ovidiu working on this one

### Task 12: Calculate the gamma decay of 22O for levels up to 6 MeV and compare to experiment. Calculate the B(E2) for Coulex to the 2(+,1) state in 22O and compare with experiment.
Shane, Ovidiu working on this one

### Task 13: Calculate the magnetic moment for the 1/2(+,1) ground state of 23O and compare to the single-particle (Schmidt) value.

### Task 14: Calculate the Fermi (F) and Gamow-Teller (GT) beta decay of 22O. The experimental energy of the lowest 1+ state in 22 F is 1.627 MeV. Compare the summed B(F) and B(GT) values to that expected from the sum-rules. What fraction of the GT sum-rule is in the transition to the lowest energy 1+ state?
