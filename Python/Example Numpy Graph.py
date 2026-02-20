import numpy as np
import matplotlib.pyplot as plt

# Time array
t = np.linspace(0, 10, 500)

# Position (e.g., s = t^3 - 5t^2 + 2t)
position = t**3 - 5*t**2 + 2*t

# Velocity is the derivative of position (ds/dt)
velocity = np.gradient(position, t)

# Acceleration is the derivative of velocity (d^2s/dt^2)
acceleration = np.gradient(velocity, t)

# Jerk is the derivative of acceleration (d^3s/dt^3)
jerk = np.gradient(acceleration, t)

# Create the plots
fig, axs = plt.subplots(4, 1, figsize=(8, 12))

# Position vs Time
axs[0].plot(t, position, label='Position', color='blue')
axs[0].set_ylabel('Position (m)')
axs[0].set_title('Position vs. Time')
axs[0].grid(True)

# Velocity vs Time
axs[1].plot(t, velocity, label='Velocity', color='green')
axs[1].set_ylabel('Velocity (m/s)')
axs[1].set_title('Velocity vs. Time')
axs[1].grid(True)

# Acceleration vs Time
axs[2].plot(t, acceleration, label='Acceleration', color='red')
axs[2].set_ylabel('Acceleration (m/s²)')
axs[2].set_title('Acceleration vs. Time')
axs[2].grid(True)

# Jerk vs Time
axs[3].plot(t, jerk, label='Jerk', color='purple')
axs[3].set_ylabel('Jerk (m/s³)')
axs[3].set_xlabel('Time (s)')
axs[3].set_title('Jerk vs. Time')
axs[3].grid(True)

plt.tight_layout()
plt.show()