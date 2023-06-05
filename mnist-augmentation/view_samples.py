import os
import argparse
from random import randint

from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='.', type=str, help='root directory of dataset where MNIST/raw/* exist')
parser.add_argument('--nrows', default=1, type=int, help='number of rows in the plot')
parser.add_argument('--ncols', default=1, type=int, help='number of columns in the plot')
parser.add_argument('--test', action='store_false', dest='train', help='set flag to view samples from test file')
args = parser.parse_args()

assert os.path.exists(f'{args.root}/MNIST/raw'), f'{args.root}/MNIST/raw does not exist, check the root path'
mnist = MNIST(args.root, download=False, train=args.train, transform=ToTensor()) 

fig = plt.figure(figsize=(8, 8))
for i in range(1, args.nrows*args.ncols+1):
    idx = randint(0, len(mnist)+1)
    img, label = mnist[idx]
    fig.add_subplot(args.nrows, args.ncols, i)
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title(label)
    plt.axis('off')
plt.show()