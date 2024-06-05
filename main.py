# This is a sample Python script.
from pygments.formatters import img

from Image import auto_corell
from Image import CanauxDeCouleur
from Predicteur import gauss
import cv2
import numpy as np
import matplotlib.pyplot as plt

image="lena15.jpg"

M=auto_corell(image)

def R(M):
    A=np.zeros((6,6))
    b=np.zeros(6)
    x=0

    for i in range(6):
        t=i%2
        l = x
        for j in range(6):
            w = j % 2
            b[i] = M[l][1-t]
            terme = M[l][2 +t+(-1)**i*w]
            A[i][j]=terme
            if w == 1:
                l += 1
        if t==1:
            x+=3

    r=gauss(A,b)

    return r

def G(M):
    A=np.zeros((7,7))
    b=np.zeros(7)
    x=0

    for i in range(6):
        t=i%2
        l = x+1
        for j in range(6):
            w = j % 2
            b[i] = M[l][1-t]
            terme = M[l][2 +t+(-1)**i*w]
            A[i][j]=terme
            if w == 1:
                l += 1
        if t==1:
            x+=3
    for i in range(6):
        A[i][6]=M[1-i%2][(i//2)*2]
    for j in range(6):
        A[6][j]=M[][0]

    g=gauss(A,b)

    return g


def B(M):
    A=np.zeros((8,8))
    b=np.zeros(8)
    x=0

    for i in range(6):
        t=i%2
        l = x+2
        for j in range(6):
            w = j % 2
            b[i] = M[l][1-t]
            terme = M[l][2 +t+(-1)**i*w]
            A[i][j]=terme
            if w == 1:
                l += 1
        if t==1:
            x+=3
    for i in range(7):
        A[i][6]=M[][0]
    for j in range(6):
        A[6][j]=M[][0]

    for i in range(8):
        A[i][7]=M[][1]
    for j in range(8):
        A[7][j]=M[][1]
    b=gauss(A,b)

    return b

def reco_R(image,r,g,b):
    img = cv2.imread(image)
    Predit=np.zeros(img.shape)
    R,G,B=CanauxDeCouleur(image)

    for i in range(1,img.shape[0]):
        for j in range(1,img.shape[1]):
            Predit[i][j][0]=int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])
            Predit[i][j][1]=int(g[0]*R[i-1][j]+g[1]*R[i][j-1]+g[2]*G[i-1][j]+g[3]*G[i][j-1]+g[4]*B[i-1][j]+g[5]*B[i][j-1]+g[6]*Predit[i][j][0])
            Predit[i][j][2]=int(b[0]*R[i-1][j]+b[1]*R[i][j-1]+b[2]*G[i-1][j]+b[3]*G[i][j-1]+b[4]*B[i-1][j]+b[5]*B[i][j-1]+b[6]*Predit[i][j][0]+b[7]*Predit[i][j][1])


    return Predit


if __name__ == '__main__':


    r,g,b=R(M),G(M),B(M)
    Predit=reco_R(image,r,g,b)

    img=cv2.imread(image)



