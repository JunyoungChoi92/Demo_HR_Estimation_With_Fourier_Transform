import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import BarycentricInterpolator

# Function to create a PPG-like signal
def create_ppg_like_signal(time):
    return np.sin(2 * np.pi * time) - 0.5 * np.sin(4 * np.pi * time) + 0.2 * np.sin(6 * np.pi * time)

def create_ppg_like_signal_with_variation(time, variation_strength=0.1):
    random_variation = np.random.normal(0, variation_strength, size=time.shape)
    return create_ppg_like_signal(time) + random_variation

# Original time points and PPG data
time_original = np.linspace(0, 3, num=108, endpoint=True)
ppg_original = create_ppg_like_signal_with_variation(time_original)
time_upsampled = np.linspace(0, 3, num=108, endpoint=True)

# Polynomial interpolation
polynomial_interpolator = BarycentricInterpolator(time_original, ppg_original)
ppg_upsampled_polynomial = polynomial_interpolator(time_upsampled)

# Plotting the first graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(time_original, ppg_original, 'o', label='Original Data')
plt.plot(time_upsampled, ppg_upsampled_polynomial, '-', label='Up-sampled Data (Polynomial)')
plt.title('(WD)PPG Data Up-sampling with Polynomial Interpolation')
plt.xlabel('Time (seconds)')
plt.ylabel('PPG Signal Amplitude')
plt.legend()

# Data for second plot
num_points = 50
time_original_1s_phase = np.linspace(0, 3, num=num_points, endpoint=True)
ppg_original_1s_phase = create_ppg_like_signal(time_original_1s_phase)
time_upsampled_1s_phase = np.linspace(0, 3, num=50, endpoint=True)

# Polynomial interpolation for second plot
polynomial_interpolator_1s_phase = BarycentricInterpolator(time_original_1s_phase, ppg_original_1s_phase)
ppg_upsampled_1s_phase = polynomial_interpolator_1s_phase(time_upsampled_1s_phase)

# Plotting the second graph
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot

# Plotting only the 16th, 32nd, and 48th values of the original data
selected_indices = [0, 15, 31, 47]
plt.plot(time_original_1s_phase[selected_indices], ppg_original_1s_phase[selected_indices], 'o', label='Selected Original Data Points')

plt.plot(time_upsampled_1s_phase, ppg_upsampled_1s_phase, '-', label='Up-sampled Data (Polynomial)')
plt.title('(MD)PPG Data Up-sampling with Polynomial Interpolation (1-second intervals, 3-second phase)')
plt.xlabel('Time (seconds)')
plt.ylabel('PPG Signal Amplitude')
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()