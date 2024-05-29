import cv2
import numpy as np
import matplotlib.pyplot as plt

def CanauxDeCouleur(image):
    img = cv2.imread(image)

    canal_rouge=img[:,:,0]
    canal_vert=img[:,:,1]
    canal_bleu=img[:,:,2]

    return canal_rouge,canal_vert,canal_bleu

img= "lena15.jpg"


def auto_corell():
    canal_R, canal_G, canal_B = CanauxDeCouleur(img)
    l,w = np.shape(canal_R)
    col = 0
    ligne = 0
    Moyenne=[]


    for f1 in ["R","G","B"]:
        for f2 in ["R", "G", "B"]:

            if f1=="R":
                canal_1=canal_R
            elif f1=="G":
                canal_1=canal_G
            elif f1=="B":
                canal_1=canal_B

            if f2=="R":
                canal_2=canal_R
            elif f2=="G":
                canal_2=canal_G
            elif f2=="B":
                canal_2=canal_B


            for i in range(1,l-1):
                for j in range(1, w-1):
                    col += canal_1[i,j]*canal_2[i-1,j]
                    ligne += canal_1[i,j]*canal_2[i,j-1]
            N=(l-2)*(w-2)
            moyenne_col = col/N
            moyenne_ligne=ligne/N

            Moyenne.append([moyenne_ligne,moyenne_col])

    return Moyenne


print(auto_corell())
















