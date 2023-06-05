from torch import randint, norm
from torchvision.transforms import ToTensor
from torchvision.transforms.functional import get_dimensions


class RandomColor:

    def __init__(self, radius):

        self.radius = radius

    def random_color(self, center=None):

        color = randint(0, 256, (3,))
        if center is not None:
            while norm((color-center).double(), p=2) < self.radius:
                color = randint(0, 256, (3,))
        return color

    def __call__(self, img):

        background = self.random_color()
        out = background.repeat(*get_dimensions(img)[-2:], 1).permute(2, 0, 1)

        indices = img.nonzero()[:, 1:].tolist()
        for h, w in indices:
            out[:, h, w] = img[0, h, w]*self.random_color(center=background) + (1-img[0, h, w])*background

        return out


if __name__ == '__main__':

    import os
    import argparse
    import random
    
    from torchvision.datasets import MNIST
    import matplotlib.pyplot as plt

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.', type=str, help='root directory of dataset where MNIST/raw/* exist')
    parser.add_argument('--radius', default=100, type=int, help='min distance between object and background pixel values')
    args = parser.parse_args()

    assert os.path.exists(f'{args.root}/MNIST/raw'), f'{args.root}/MNIST/raw does not exist, check the root path'
    mnist = MNIST(args.root, download=False, train=True, transform=ToTensor()) 

    fig = plt.figure(figsize=(8, 8))

    img, label = mnist[random.randint(0, len(mnist)+1)]
    fig.add_subplot(1, 2, 1)
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title(f'Original, label = {label}')
    plt.axis('off')

    transformed_img = RandomColor(radius=args.radius)(img)
    fig.add_subplot(1, 2, 2)
    plt.imshow(transformed_img.permute(1, 2, 0))
    plt.title(f'Radius = {args.radius}')
    plt.axis('off')

    plt.show()