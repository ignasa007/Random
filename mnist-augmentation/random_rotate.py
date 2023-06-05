from torch import Tensor
from torchvision.transforms import RandomRotation
from torchvision.transforms.functional import InterpolationMode, get_dimensions, rotate

class RandomRotation(RandomRotation):

    def __init__(self, degrees, interpolation=InterpolationMode.NEAREST, expand=False, center=None, fill=0):

        super().__init__(degrees, interpolation=interpolation, expand=expand, center=center, fill=fill)

    def forward(self, img):

        fill = self.fill
        channels, _, _ = get_dimensions(img)
        if isinstance(img, Tensor):
            if isinstance(fill, (int, float)):
                fill = [float(fill)] * channels
            else:
                fill = [float(f) for f in fill]
        angle = self.get_params(self.degrees)

        return rotate(img, angle, self.interpolation, self.expand, self.center, fill), angle

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
    parser.add_argument('--degrees', default=25, type=int, help='max degrees to rotate clockwise or counter-clockwise')
    args = parser.parse_args()

    assert os.path.exists(f'{args.root}/MNIST/raw'), f'{args.root}/MNIST/raw does not exist, check the root path'
    mnist = MNIST(args.root, download=False, train=True, transform=ToTensor()) 

    fig = plt.figure(figsize=(8, 8))

    img, label = mnist[randint(0, len(mnist)+1)]
    fig.add_subplot(1, 2, 1)
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title(f'Original, label = {label}')
    plt.axis('off')

    transformed_img, angle = RandomRotation(degrees=args.degrees)(img)
    fig.add_subplot(1, 2, 2)
    plt.imshow(transformed_img.squeeze(), cmap='gray')
    plt.title(f'Rotated at {angle:.3f} degrees')
    plt.axis('off')

    plt.show()