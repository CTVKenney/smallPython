#!/usr/bin/env python3

"""
Practice with PyTorch
"""

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

#Download 
"""
training_data = datasets.FashionMNIST(
    root='data',
    train=True,
    download=True,
    transform=ToTensor(),
)

test_data = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True
    transform=ToTensor(),
)
"""



def main():
    return

if __name__ = '__main__':
    main()
