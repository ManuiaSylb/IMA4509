# This is a sample Python script.
from Image import auto_corell
from Predicteur import gauss
import cv2
import numpy as np

image="lena15.jpg"

def creation_systeme_R():
    A=[]
    b=np.zeros_like([6,1])
    c=np.zeros_like([6,1])
    M=auto_corell(image)

    for i in range(6):
        A.append([])




if __name__ == '__main__':
