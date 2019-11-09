import matplotlib
import matplotlib.pyplot as plt
import numpy as np

q1 = float (1 * 10**-9)
q2 = float(1 * 10**-9)
k = float(9 * 10**9)

# Data for plotting
r = np.arange(1,5,0.01)
f = k * ((q1*q2)/(r*r))

fig, ax = plt.subplots()
ax.plot(r, f)

ax.set(xlabel='r (m)', ylabel='F (N)', title='Coulombov zakon (ovisnost o udaljenosti)')
ax.grid(b='false')

ax.set_yticklabels([])
ax.set_xticklabels([])

#fig.savefig("coulombov_zakon1.png")
plt.show()