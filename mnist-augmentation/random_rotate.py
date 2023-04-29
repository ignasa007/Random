from torch import Tensor
import torchvision.transforms as T
import torchvision.transforms.functional as F

class RandomRotation(T.RandomRotation):

    def __init__(self, degrees, interpolation=F.InterpolationMode.NEAREST, expand=False, center=None, fill=0):

        super().__init__(degrees, interpolation=interpolation, expand=expand, center=center, fill=fill)

    def forward(self, img):

        fill = self.fill
        channels, _, _ = F.get_dimensions(img)
        if isinstance(img, Tensor):
            if isinstance(fill, (int, float)):
                fill = [float(fill)] * channels
            else:
                fill = [float(f) for f in fill]
        angle = self.get_params(self.degrees)

        return F.rotate(img, angle, self.interpolation, self.expand, self.center, fill), angle

if __name__ == '__main__':

    import os
    import argparse

    from torch import randint
    from torchvision.datasets import MNIST
    import matplotlib.pyplot as plt

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.', type=str, help='root directory of dataset where MNIST/raw/* exist')
    parser.add_argument('--degrees', default=25, type=int, help='max degrees to rotate clockwise or counter-clockwise')
    args = parser.parse_args()

    assert os.path.exists(f'{args.root}/MNIST/raw'), f'{args.root}/MNIST/raw does not exist, check the root path'
    mnist = MNIST(args.root, download=False, train=True, transform=T.ToTensor()) 

    fig = plt.figure(figsize=(8,8))

    img, _ = mnist[randint(len(mnist), size=(1,)).item()]
    fig.add_subplot(1, 2, 1)
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title('Original')
    plt.axis('off')

    transformed_img, angle = RandomRotation(degrees=args.degrees)(img)
    fig.add_subplot(1, 2, 2)
    plt.imshow(transformed_img.squeeze(), cmap='gray')
    plt.title(f'Rotated at {angle:.3f} degrees')
    plt.axis('off')

    plt.show()