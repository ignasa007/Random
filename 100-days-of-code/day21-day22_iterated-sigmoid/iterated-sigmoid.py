import os
import shutil
import glob
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

sigmoid = lambda x: 1 / (1 + np.exp(-x))
x_lim, steps, num_times = 8, 5, 2

data = [np.linspace(-x_lim, x_lim, 1000)]
for _ in range(10):
    x = data[-1]
    x = x_lim * (2*(x-np.min(x))/(np.max(x)-np.min(x)) - 1)
    data.append(sigmoid(x))
x, *data = data

frame_folder = 'assets'
os.makedirs(frame_folder, exist_ok=True)

indices = list(range(steps)) + list(range(steps-1, -1, -1))
pause = 0.2

for frame, i in enumerate(indices*num_times):
    plt.clf()
    plt.title(f'Sigmoid, iter={i+1}')
    plt.scatter(x, data[i], s=15)
    plt.grid()
    plt.savefig(os.path.join(frame_folder, f"{str(frame).rjust(2, '0')}.jpg"))
    plt.pause(pause)
plt.show()

frames = [Image.open(image) for image in glob.glob(f'{frame_folder}/*.jpg')]
frame_one = frames[0]
frame_one.save('iterated-sigmoid.gif', format='GIF', append_images=frames, save_all=True, duration=pause*1000, loop=0)

shutil.rmtree(frame_folder)