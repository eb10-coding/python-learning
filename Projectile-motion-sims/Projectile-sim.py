"""
Projectile Motion Simulator - No Drag (Euler's Method)

Simulates 2D projectile motion under gravity only, using Euler's
method for numerical integration rather than analytical SUVAT formulas.
"""

import numpy as np
import matplotlib.pyplot as plt



# Constants

GRAVITY = 9.81      # acceleration due to gravity (m/s^2)
TIME_STEP = 0.01    # size of each simulation step (s)



# User input

initial_speed = float(input("Enter launch speed (m/s): "))
launch_angle_deg = float(input("Enter launch angle (degrees): "))



# Initial conditions

launch_angle_rad = np.radians(launch_angle_deg)

velocity_x = initial_speed * np.cos(launch_angle_rad)
velocity_y = initial_speed * np.sin(launch_angle_rad)

position_x = 0
position_y = 0
elapsed_time = 0

# lists to store the trajectory
x_positions = [position_x]
y_positions = [position_y]



# Simulation loop (Euler's method)

while position_y >= 0:
    # update velocity:
    velocity_y = velocity_y - GRAVITY * TIME_STEP

    # update position
    position_x = position_x + velocity_x * TIME_STEP
    position_y = position_y + velocity_y * TIME_STEP

    # advance the clock
    elapsed_time += TIME_STEP

    # record this step's position
    x_positions.append(position_x)
    y_positions.append(position_y)



# Plot the results

plt.plot(x_positions, y_positions)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion (No Drag, Euler's Method)")
plt.grid(True)
plt.show()