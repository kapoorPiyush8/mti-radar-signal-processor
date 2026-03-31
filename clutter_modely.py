#clutter modelling 
#31 March
import math
def sec(x):
  return 1/np.cos(x)

#analytical verification

R=50*1000 #km ->m
theta_3dB=2*(3.141)/180 # to radians 
c=3e8 # m/s
tau = 1e-6 #pulse width
psi=3*(3.141)/180
A_c=R*theta_3dB*sec(psi)*c*tau/2
print(A_c)
A_c_dB=10*math.log10(A_c)
#for open farmland clutter coeffcient = -20dB
#clutter power = 54.2dB-20dB = 34.2dB

import numpy as np
def compute_clutter (R, theta_3dB_deg, psi_deg, tau, sigma0_dB):
  theta = theta_3dB_deg*(np.pi)/180
  psi = psi_deg*(np.pi)/180
  c=3e8
  A_c= R*theta*(c*tau/2)*sec(psi)
  A_c_dB=10*np.log10(A_c)
  clutter_RCS_dB= sigma0_dB+A_c_dB
  return A_c, A_c_dB,clutter_RCS_dB

#parameters
R=50e3
theta_3dB_deg=2
tau=1e-6
psi_deg=3
sigma0_dB=-20
target_RCS_dBsm=0 

A_c, A_c_dB, clutter_RCS_dB=compute_clutter(R, theta_3dB_deg, psi_deg, tau,sigma0_dB)
SCR= target_RCS_dBsm-clutter_RCS_dB
print("Clutter Area A_c = ", A_c, "m^2")
print("Clutter Area A_c (in dB) = ", A_c_dB, "dBsm")
print("Clutter RCS = ", clutter_RCS_dB, "dBsm")
print ("SCR before MTI = ", SCR, "dBsm")

import matplotlib.pyplot as plt

# Range array
R_array = np.linspace(1e3, 100e3, 500)  # 1km to 100km

# Compute clutter over range
SCR_array = []
for R in R_array:
    A_c, A_c_dB, clutter_RCS_dB = compute_clutter(R, theta_3dB_deg, psi_deg, tau, sigma0_dB)
    SCR = target_RCS_dBsm - clutter_RCS_dB
    SCR_array.append(SCR)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(R_array/1e3, SCR_array)
plt.axhline(y=0, color='red', linestyle='--', label='SCR = 0 dB')
plt.xlabel('Range (km)')
plt.ylabel('SCR (dB)')
plt.title('Signal to Clutter Ratio vs Range (Before MTI)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

