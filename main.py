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

    return A,b

def reco_R(image,r):
    img = cv2.imread(image)
    R_predit=np.zeros(img.shape)
    R,G,B=CanauxDeCouleur(image)

    for i in range(1,img.shape[0]):
        for j in range(1,img.shape[1]):
            R_predit[i][j][0]=int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])
            R_predit[i][j][1]=int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])
            R_predit[i][j][2]=int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])

    return R_predit


if __name__ == '__main__':

    A,b=R(M)
    r=gauss(A,b)
    R_predit=reco_R(image,r)
    print(R_predit[:,:,0])
    print(CanauxDeCouleur(image)[0])


    img=cv2.imread(image)

    while True:
        cv2.imshow('canal-rouge',CanauxDeCouleur(image)[0])
        cv2.imshow('Predit',R_predit)
        if cv2.waitKey(0):
            break

    cv2.destroyAllWindows()

