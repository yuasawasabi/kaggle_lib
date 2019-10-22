'''This is capsule net module
   this is made based on Understanding Hinton's Capsule Networks'''
import torch
import torch.nn as nn
import torch.nn.functional as f
import torchvision

class CapsuleNet(nn.Module):
    """This is a prototype of capsulenet"""
    def __init__(self):
        super().__init__()
        
        
        

    def p_n(self):
        """test to import"""
        print('Capsnet is imported')

class PrimaryCapsule(nn.Module):
    """Primary Capsule Class"""
    def __init__(self):
        super().__init__()

class DigitCapsule(nn.Module):
    """Digit Capsule Class"""
    def __init__(self):
        super().__init__()


def loss_function_for_capusule_net():
    """loss function for capsule net"""
    return None

def routing_algorithm(u, r, l):
    """routing algorithm"""
    print("routing algorithm is running")
    return None

if __name__ == '__main__':
    C = CapsuleNet()
    C.p_n()
