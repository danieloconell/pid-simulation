import numpy as np
import matplotlib.pyplot as plt

# Pid values
dt = 0.1
Kp = 10
Ki = 0
Kd = 470

x = v = i = d = o = 0
sp = 1
e = last_e = sp-x

times = np.arange(0, 10, dt)
positions = []
set_points = [sp] * len(times)

for time in times:
    x = x + dt * v
    v = v + dt * o
    e = sp - x
    d = dt * (e - last_e)
    i = i + e * dt
    o = Kp*e + Ki*i + Kd*d
    pid = np.array([x, v, e, d, i])
    last_e = e
    positions.append(x)

plt.plot(times, positions, "b-", times, set_points, "r-")
plt.show()
