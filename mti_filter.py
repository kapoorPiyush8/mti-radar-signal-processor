import numpy as np

PRF=1000 #1kHz
PRI=1/PRF
T=PRI
f_doppler = np.linspace(-PRF/2, PRF/2, 1000)
omega = 2*np.pi*f_doppler  # f_doppler convert
H_single= 2*np.abs(np.sin(omega*T/2)) #for negative sign the axes can become negative but mag cannot be negative add abs
H_single_dB=20*np.log10(H_single)
H_double=4*(np.sin(omega*T/2)**2)
H_double_dB=20*np.log10(H_double)


import matplotlib.pyplot as plt
plt.plot(f_doppler, H_single, label="single line canceller")
plt.plot(f_doppler, H_double, label="double line canceller")
plt.xlabel("Doppler Frequency")
plt.ylabel("Frequency Response of Delaly Line Canceller")
plt.legend()
plt.show()

plt.plot(f_doppler, H_single_dB, label="single line canceller")
plt.plot(f_doppler, H_double_dB, label="double line canceller")
plt.xlabel("Doppler Frequency")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.show()

c=3e8
fc=10e9 #10GHz
lambda_c= c/fc
vel=50 # m/s
f_doppler_c=np.linspace(-PRF/2,PRF/2,PRF)
vel_max=lambda_c*PRF/4
f_d= 2*vel/lambda_c
print("maximum velcoity = ", vel_max)
print ("doppler frequency = ", f_d)


N=64
vel_target=5 #m/s
f_d= 2*vel_target/lambda_c #doppler frequency
n=np.arange(N)
#clutter modelling linear
clutter= 100*np.ones(N)
#target model
target=1*np.exp(1j*2*np.pi*f_d*n*T)
#noise model:
noise_power=0.1
noise=np.sqrt(noise_power/2)*(np.random.randn(N)+1j*np.random.randn(N))
#signal linear model
signal=clutter+target+noise


plt.plot(n, np.real(signal), label="radar return")
plt.xlabel("Pulse index")
plt.ylabel("Magnitude (linear)")
plt.legend()
plt.show()

#7april: to be continued from here
# Single delay line canceller
mti_output = np.diff(signal)  # numpy ka diff function exactly ye karta hai

plt.figure(figsize=(10,4))
plt.plot(n[1:], np.real(mti_output), label="After MTI")
plt.xlabel("Pulse index")
plt.ylabel("Magnitude (linear)")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(n[1:], np.real(mti_output), label="After MTI")
plt.plot(n, np.real(signal), label="Before MTI")
plt.xlabel("Pulse index")
plt.ylabel("Magnitude (linear)")
plt.legend()
plt.grid(True)
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

ax1.plot(n, np.real(signal), color='orange', label='Before MTI')
ax1.set_ylabel('Magnitude (linear)')
ax1.legend()
ax1.grid(True)

ax2.plot(n[1:], np.real(mti_output), color='blue', label='After MTI')
ax2.set_ylabel('Magnitude (linear)')
ax2.set_xlabel('Pulse index')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

plt.savefig('plots/mti_response.png', dpi=150, bbox_inches='tight')
