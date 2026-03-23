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
