#14April 2D signal reconstruction for range doppler
n_range_bins=1000 # delta_R=150m, max range=150km
n_pulses=64
target_bin=334 # taget is at 50km, bin_index= 50*1000/150
#initialize signal
signal_2d=np.zeros((n_range_bins,n_pulses),dtype=complex)
#add clutter
signal_2d+=10*np.ones((n_range_bins,n_pulses),dtype=complex) #reduced from 100 to 10; 15 april
#add noise
noise_power=0.1
noise=np.sqrt(noise_power/2)*(np.random.randn(n_range_bins,n_pulses)+1j*np.random.randn(n_range_bins,n_pulses))
signal_2d+=noise
#target at range 334
signal_2d[target_bin,:]+=10*np.exp(1j*2*np.pi*f_d*n*T) #changed from 1 to 10; 15 april

mti_2d=np.diff(signal_2d,axis=1)
print(mti_2d.shape)

rd_map = np.fft.fft(mti_2d, axis=1)
rd_map = np.fft.fftshift(rd_map, axes=1)

#15 April
plt.figure(figsize=(12,6))
plt.imshow(20*np.log10(np.abs(rd_map[200:500, :])),
           aspect='auto', origin='lower')
plt.colorbar(label='Magnitude (dB)')
plt.xlabel('Doppler bin')
plt.ylabel('Range bin')
plt.title('Range-Doppler Map - Zoomed')
plt.show()

