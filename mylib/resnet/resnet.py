'''This is residual net module'''
import torch
import torch.nn as nn
import torch.nn.functional as f
import torchvision

class ResidualPlainBlock(nn.Module):
    """basic block for resnet"""
    def __init__(self, in_ch, out_ch, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_ch, out_ch, kernel_size=3, stride=stride)
        self.bn1 = nn.BatchNorm2d(out_ch)
        self.conv2 = nn.Conv2d(out_ch, out_ch, kernel_size=3, stride=stride)
        self.bn2 = nn.BatchNorm2d(out_ch)

        self.shortcut = nn.Sequential()
        if in_ch != out_ch:
            self.shortcut.add_module('conv', nn.Conv2d(in_ch, out_ch, kernel_size=1, stride=stride))
            self.shortcut.add_module('bn', nn.BatchNorm2d(out_ch))

    def forward(self, x):
        out = f.relu((self.bn1(self.conv1(x))))
        out = f.relu((self.bn2(self.conv2(out))))
        out += self.shortcut(x)
        return out
