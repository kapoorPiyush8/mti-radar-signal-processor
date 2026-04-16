import numpy as np

def ca_cfar(signal, n_guard, n_train, alpha):
    """
    CA-CFAR detector
    signal: 1D complex array
    returns: detection indices
    """
    N = len(signal)
    detections = []
    for i in range(n_guard + n_train, N - n_guard - n_train):
        left = signal[i - n_guard - n_train : i - n_guard]
        right = signal[i + n_guard + 1 : i + n_guard + n_train + 1]
        noise_est = (np.sum(np.abs(left)**2) + np.sum(np.abs(right)**2)) / (2 * n_train)
        threshold = alpha * noise_est
        if np.abs(signal[i])**2 > threshold:
            detections.append(i)
    return detections

# Detection in Doppler domain
detections = ca_cfar(doppler_spectrum_shifted, n_guard=2, n_train=4, alpha=6)
print("Detections:", detections)
