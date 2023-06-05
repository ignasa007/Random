from torch import Tensor, rand
from torchvision.transforms import RandomPerspective
import torchvision.transforms.functional as F

class RandomPerspective(RandomPerspective):

    def __init__(self, distortion_scale=0.5, interpolation=F.InterpolationMode.BILINEAR, fill=0):

        super().__init__(distortion_scale=distortion_scale, p=1.0, interpolation=interpolation, fill=fill)

    def forward(self, img):

        fill = self.fill
        channels, height, width = F.get_dimensions(img)
        if isinstance(img, Tensor):
            if isinstance(fill, (int, float)):
                fill = [float(fill)] * channels
            else:
                fill = [float(f) for f in fill]

        startpoints, endpoints = self.get_params(width, height, self.distortion_scale)

        return F.perspective(img, startpoints, endpoints, self.interpolation, fill), startpoints, endpoints

if __name__ == '__main__':

    import os
    import argparse
    from random import randint
    
    from torchvision.datasets import MNIST
    from torchvision.transforms import ToTensor
    import matplotlib.pyplot as plt

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.', type=str, help='root directory of dataset where MNIST/raw/* exist')
    parser.add_argument('--distortion_scale', default=0.5, type=str, help='argument to control degree of distortion')
    args = parser.parse_args()

    assert os.path.exists(f'{args.root}/MNIST/raw'), f'{args.root}/MNIST/raw does not exist, check the root path'
    mnist = MNIST(args.root, download=False, train=True, transform=ToTensor()) 

    fig = plt.figure(figsize=(8, 8))

    img, label = mnist[randint(0, len(mnist)+1)]
    fig.add_subplot(1, 2, 1)
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title(f'Original, label = {label}')
    plt.axis('off')

    transformed_img, startpoints, endpoints = RandomPerspective(distortion_scale=args.distortion_scale)(img)
    fig.add_subplot(1, 2, 2)
    plt.imshow(transformed_img.squeeze(), cmap='gray')
    plt.title(f'End points: {endpoints}')
    plt.axis('off')

    plt.show()