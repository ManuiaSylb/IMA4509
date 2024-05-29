import cv2
import numpy as np
import matplotlib.pyplot as plt

def CanauxDeCouleur(image):
    img = cv2.imread(image)

    canal_rouge=img[:,:,0]
    canal_vert=img[:,:,1]
    canal_bleu=img[:,:,2]

    return canal_rouge,canal_vert,canal_bleu
