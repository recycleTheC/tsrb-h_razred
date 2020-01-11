# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

r = 1
k = float(9 * 10**9)

# Data for plotting
q2 = np.arange(0 , (5*10**-9), 0.01*10**-9)**2
f = k * ((q2)/(r*r))

fig, ax = plt.subplots()
ax.plot(q2, f)

ax.set(xlabel='Q1*Q2 (C)', ylabel='F (N)', title=u'Coulombov zakon (ovisnost o količini naboja, Q1 = Q2)')
ax.grid(b='false')

ax.set_yticklabels([])
ax.set_xticklabels([])

plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.show()