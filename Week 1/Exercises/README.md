# Exercise set 1 - solutions

### Ex 1: Use aud16.dat find all known nuclei that are unbound to two-proton decay but bound to one-proton decay.
Use 2p_unbound.py (which uses aud16.dat) to calculate two proton and one proton separation energies of the nuclei in aud16.dat. The result is that four nuclei are unbound to two-proton decay but bound to one-proton decay. They are:
(Z,N) = (4,6), (12,19), (80,172) and (82,188).

TODO: physical explanation?

### Ex 2: Use the liquid-drop model to obtain the neutron drip line for Z=36-44. Compare to the HFB-27 model and comment on the reasons for the difference.
The program "n_drip_Shane.py" calculates the neutron dripline for Z=36-44. The result is:

|  N  |  Z  |
|-----|-----|
| 36  | 94  |
| 37  | 96  |
| 38  | 99  |
| 39  | 102 |
| 40  | 104 |
| 41  | 107 |
| 42  | 109 |
| 43  | 112 |
| 44  | 114 |

TODO: compare with HFB-27

### Ex 3: Use rms13.dat to obtained the differences in charge radii for N and N-1 and make a plot vs neutron number N. Comment on the result. This is known as the Brix-Kopferman plot.
The differences in charge radii for N and N-1 were calculated by using the program rms_radii.py. The results are shown in the following figure (Hg and Y are highlighted)

![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Week%201/Exercises/rmsdata.pdf)


### Ex 4: Use toiee.dat to make a plot of the ratio of the 8+ to 6+ energies for yrast states. Comment on your results.

### Ex 5: Calculate the 14C decay Q value of 223Ra. Use this to estimate the half-life and compare to experiment. What is the branching ratio for the 14C decay?

# External e-mail exercise

### Na23 levels
![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Week%201/Exercises/na23y.png)

### Comparison between experiments and theory (cceisdpn)
The lowest states are pretty well produced, but in overall theory could give more accurate results.

### Mg23 levels
![alt text](https://github.com/tikrneva/Talent2017-Group6/blob/master/Week%201/Exercises/mg23y.png)
