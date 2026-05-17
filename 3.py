import numpy as np
import matplotlib.pyplot as plt
import imageio
from io import BytesIO

u = np.loadtxt(r'C:\Users\User\Desktop\2 курс\информатика\np-20260429T194436Z-3-001\np\3.dat')
N = len(u)

A = np.eye(N)
A += np.diag(-np.ones(N-1), k=-1)
A[0, N-1] = -1

steps = 255
frames = []

u_current = u.copy()
for step in range(steps + 1):
    plt.figure(figsize=(8, 4))
    plt.plot(u_current)
    plt.title(f'Шаг {step}')
    plt.grid(True)
    plt.ylim(0, 11)
    

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames.append(imageio.imread(buf))
    plt.close()
    
    if step < steps:
        u_current = u_current - 0.5 * A @ u_current

imageio.mimsave('3.gif', frames, duration=0.5)
