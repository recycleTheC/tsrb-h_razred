# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

r = np.arange(1, 8, 0.0001)
k = float(9 * 10**9)
radius = 2

# Data for plotting
q = 50*10**-9
e = k * (q/(r*r))

fig, ax = plt.subplots()
ax.plot(r, e, 'r')

ax.set(xlabel='r (m)', ylabel='E (N/C)', title=u'Jakost električnog polja metalne kugle\n(ovisnost o udaljenosti)')
ax.grid(b='false')

ax.set_yticklabels([])
ax.set_xticklabels(['0','R'])

plt.xlim(xmin=0)
plt.ylim(ymin=0)

x1 = [1,1]
x2 = [0,449]

plt.plot(x1,x2, 'r')
plt.plot([0,0], 'r')

plt.show()