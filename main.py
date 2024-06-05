# This is a sample Python script.
from Image import auto_corell
from Predicteur import gauss
import cv2
import numpy as np

image="lena15.jpg"

M=auto_corell(image)

def R(M):
    A=np.zeros((6,6))
    b=np.zeros(6)
    l=0

    for i in range(6):
        t=i%2
        l=0
        for j in range(6):
            w = j % 2
            b[i] = M[l][1-t]
            terme = M[l][2 +t+(-1)**i*w]
            A[i][j]=terme
            if w == 1:
                l += 1
        l+=3

    return A,b




if __name__ == '__main__':
    A,b=R(M)
    print(A,b)
