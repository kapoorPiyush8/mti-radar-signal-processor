import numpy as np

# Radar Parameters
fc = 10e9          # Carrier frequency (Hz) - X band
c = 3e8            # Speed of light
PRF = 1000         # Pulse repetition frequency (Hz)
PRI = 1/PRF        # Pulse repetition interval (s)
tau = 1e-6         # Pulse width (s)
wavelength = c/fc  # Lambda

# Derived Parameters
R_max = (c * PRI) / 2
V_max = (wavelength * PRF) / 4

print(f"Wavelength: {wavelength*1000:.2f} mm")
print(f"Max Unambiguous Range: {R_max/1000:.1f} km")
print(f"Max Unambiguous Velocity: {V_max:.2f} m/s")

# Waveform Generation
fs = 100e6         # Sampling frequency (Hz)
t_pulse = np.arange(0, tau, 1/fs)  # Time array for one pulse

# Simple rectangular pulse (baseband)
pulse = np.ones(len(t_pulse))

# Full PRI with listening time
t_pri = np.arange(0, PRI, 1/fs)
waveform = np.zeros(len(t_pri))
waveform[:len(pulse)] = pulse

print(f"\nPulse samples: {len(pulse)}")
print(f"PRI samples: {len(t_pri)}")
print(f"Duty cycle: {len(pulse)/len(t_pri)*100:.2f}%")


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))
plt.plot(t_pri * 1e6, waveform)
plt.xlabel('Time (microseconds)')
plt.ylabel('Amplitude')
plt.title('Pulsed Radar Waveform - Single PRI')
plt.xlim(0, 50)
plt.grid(True)
plt.tight_layout()
plt.savefig('waveform_plot.png', dpi=150)
plt.show()

#changing the PRF to see the effect on the maximum ambiguous range and velcoity
PRF=5000
c=3e8
PRI=1/PRF
R_max=0.5*c*PRI

fc=10e9
wavelength=3e8/fc

V_max_2=(wavelength*PRF)/4
print(f"Max velocity: {V_max_2}m/s")

print(f"Max Unambiguous Range: {R_max/1000:.1f} km")

#staggered PRF concept

PRF1, PRF2 = 1000, 750
PRI1, PRI2 = 1/PRF1, 1/PRF2
n_pulses = 8  # 4 of each

pulse_times = []
t_current = 0

for i in range(n_pulses):
    pulse_times.append(t_current)
    if i % 2 == 0:
        t_current += PRI1  
    else:
        t_current += PRI2  

print("Pulse times (ms):")
for i, t in enumerate(pulse_times):
    pri_used = "PRI1" if i % 2 == 0 else "PRI2"
    print(f"Pulse {i+1}: {t*1000:.2f} ms ({pri_used})")
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 3))
for i, t in enumerate(pulse_times):
    color = 'blue' if i % 2 == 0 else 'red'
    plt.axvline(x=t*1000, color=color, linewidth=2, 
                label=f'PRI1' if i==0 else ('PRI2' if i==1 else ''))

plt.xlabel('Time (ms)')
plt.title('Staggered PRF - Pulse Timing (Blue=PRI1, Red=PRI2)')
plt.legend()
plt.grid(True)
plt.show()
        
