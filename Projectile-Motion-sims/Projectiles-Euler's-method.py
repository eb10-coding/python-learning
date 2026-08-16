import numpy as np
import matplotlib.pyplot as plt

# inputs
 
v0 = float(input("enter initial velocity m/s: "))
angle_deg = float(input("enter angle in degrees: "))
g = 9.81
dt = 0.01

# conversion to radians

angle_rad = np.radians(angle_deg)
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

x = 0
y = 0
t = 0

x_list = [x]
y_list = [y]

while y >= 0:
    vy = vy - g * dt
    x = x + vx * dt
    y = y + vy * dt
    t += dt

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list,y_list)
plt.xlabel("Horizontal distance (m)")
plt.ylabel("height")
plt.title("projectile motion ( Euler's method )")
plt.grid(True)
plt.show()

