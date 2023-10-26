import numpy as np
import mathplotlib.pyplot as plt

x = np.random.random_sample((3,))
y = np.random.random_sample((3,))
z = np.random.random_sample((3,))

cells = 100
cps = np.size(x, 0)
seg = cps - 1
i = np.linspace(0,1, cells)
t = np.linspace(0,1, cells)
b = []

bezier_x = np.zeros((1, cells))
bezier_y = np.zeros((1, cells))
bezier_z = np.zeros((1, cells))

def binom_coeff(seg, i):
  return np.math.factorial(seg)/ (np.math.factorial(i) * np.math.factorial(seg - 1))

def bernsteinFunct(seg, i , t):
  basis = np.array(binom_coeff(seg, i) * (t ** i ) * (1 - t) ** (n - i))
  return basis

for k in range(0, seg):
  b.append(bernsteinFunct(seg, i , t))
  bezier_x = bernsteinFunct(seg, i , t) * x[k] + bezier_x
  bezier_y = bernsteinFunct(seg, i , t) * y[k] + bezier_y
  bezier_z = bernsteinFunct(seg, i , t) * z[k] + bezier_z
  x += 1

for line in b:
  plt.plot(t, line)
plt.show()
