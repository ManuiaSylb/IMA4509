# This is a sample Python script.
from Image import auto_corell
from Predicteur import gauss
import cv2
import numpy as np

image="lena15.jpg"

def creation_systeme_R():
    A=np.zeros_like([6,6])
    b=np.zeros_like([6,1])
    c=np.zeros_like([6,1])
    M=auto_corell(image)

    for i in range(6):
        terme=M[]
        for j in range(6):
            A[i,j]





if __name__ == '__main__':
