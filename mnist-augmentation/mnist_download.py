import glob, shutil, os
import argparse

from torchvision.datasets import MNIST

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='.', type=str, help='data download destination')
parser.add_argument('--del_gz', action='store_true', help='set flag to keep zip files')
parser.add_argument('--overwrite', action='store_true', help='set flag to overwrite existing {args.dest}/MNIST/raw folder')
args = parser.parse_args()

data_dir = f'{args.root}/MNIST/raw'
if not os.path.exists(data_dir):
    MNIST(args.root, download=True)
elif args.overwrite:
    shutil.rmtree(data_dir)
    MNIST(args.root, download=True)

if args.del_gz:
    for gz_file in glob.glob(f'{data_dir}/*.gz'):
        os.remove(gz_file)