"""
Projectile Motion Simulator - Drag vs No Drag (Euler's Method)

Simulates 2D projectile motion two ways: once with quadratic air
resistance, once without, and plots both trajectories together for
comparison.
"""

import numpy as np
import matplotlib.pyplot as plt



# Constants

GRAVITY = 9.81          # acceleration due to gravity (m/s^2)
TIME_STEP = 0.01        # size of each simulation step (s)
DRAG_COEFFICIENT = 0.01 # controls strength of air resistance



# User input

initial_speed = float(input("Enter initial velocity (m/s): "))
launch_angle_deg = float(input("Enter angle in degrees: "))

launch_angle_rad = np.radians(launch_angle_deg)



# Simulation 1: with drag

velocity_x = initial_speed * np.cos(launch_angle_rad)
velocity_y = initial_speed * np.sin(launch_angle_rad)

position_x = 0
position_y = 0
elapsed_time = 0

drag_x_positions = [position_x]
drag_y_positions = [position_y]

while position_y >= 0:
    elapsed_time += TIME_STEP

    # current speed
    speed = np.sqrt(velocity_x**2 + velocity_y**2)

    # update velocity
    velocity_x = velocity_x - DRAG_COEFFICIENT * speed * velocity_x * TIME_STEP
    velocity_y = (velocity_y - GRAVITY * TIME_STEP
                  - DRAG_COEFFICIENT * speed * velocity_y * TIME_STEP)

    # update position
    position_x = position_x + velocity_x * TIME_STEP
    position_y = position_y + velocity_y * TIME_STEP

    drag_x_positions.append(position_x)
    drag_y_positions.append(position_y)



# Simulation 2: without drag

velocity_x_nodrag = initial_speed * np.cos(launch_angle_rad)
velocity_y_nodrag = initial_speed * np.sin(launch_angle_rad)

position_x_nodrag = 0
position_y_nodrag = 0
elapsed_time_nodrag = 0

nodrag_x_positions = [position_x_nodrag]
nodrag_y_positions = [position_y_nodrag]

while position_y_nodrag >= 0:
    # update velocity:
    velocity_y_nodrag = velocity_y_nodrag - GRAVITY * TIME_STEP

    # update position
    position_x_nodrag = position_x_nodrag + velocity_x_nodrag * TIME_STEP
    position_y_nodrag = position_y_nodrag + velocity_y_nodrag * TIME_STEP

    elapsed_time_nodrag += TIME_STEP

    nodrag_x_positions.append(position_x_nodrag)
    nodrag_y_positions.append(position_y_nodrag)



# Plot the results

plt.plot(nodrag_x_positions, nodrag_y_positions, label="No drag")
plt.plot(drag_x_positions, drag_y_positions, label="With drag")
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion (Euler's Method)")
plt.grid(True)
plt.legend()
plt.show()