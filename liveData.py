import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def update_fig(A, rects, number):
    for rect, val in zip(rects, A):
        rect.set_height(val)
        

def bubble(A):
    n = len(A)

    for i in range(n):
        swap = False
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swap = True
                if swap:
                    yield A
        if swap == False:
            break



A = np.random.randint(1, 100, 30)
generator = bubble(A)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

bar_rects = ax.bar(np.arange(1, len(A) + 1), A, align='center')

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, 1), frames=generator, interval=1,
    repeat=False)
plt.show()
