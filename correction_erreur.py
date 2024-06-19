import cv2
import numpy as np
from Image import CanauxDeCouleur
from Predicteur import gauss
from main import R
from Image import auto_corell

image="lena15.jpg"
M=auto_corell(image)

def uniform_quantizer(signal, num_levels):

    # Trouver la valeur minimale et maximale du signal
    min_val = np.min(signal)
    max_val = np.max(signal)

    # Calculer la largeur de chaque niveau de quantification
    step_size = (max_val - min_val) / num_levels

    # Quantification
    quantized_signal = np.floor((signal - min_val) / step_size) * step_size + min_val + step_size / 2

    return quantized_signal


def uniform_dequantizer(quantized_signal, num_levels):

    # Trouver la valeur minimale et maximale du signal quantifié
    min_val = np.min(quantized_signal)
    max_val = np.max(quantized_signal)

    # Calculer la largeur de chaque niveau de quantification
    step_size = (max_val - min_val) / num_levels

    # Déquantification
    dequantized_signal = np.floor((quantized_signal - min_val) / step_size) * step_size + min_val + step_size / 2

    return dequantized_signal



def codage_DPCM(x, H, W, step,r):
    img = cv2.imread(x)
    R, G, B = CanauxDeCouleur(x)
    err_R = np.zeros((H, W), dtype=int)
    err_G = np.zeros((H, W), dtype=int)
    err_B = np.zeros((H, W), dtype=int)
    previous_pixel = 0

    for i in range(H):
        for j in range(W):
            current_pixel_R = img[i, j, 0]
            current_pixel_G = img[i, j, 1]
            current_pixel_B = img[i, j, 2]
            difference_R = current_pixel_R - int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])
            difference_G = current_pixel_G - int(g[0]*R[i-1][j]+g[1]*R[i][j-1]+g[2]*G[i-1][j]+g[3]*G[i][j-1]+g[4]*B[i-1][j]+g[5]*B[i][j-1]+g[6]*R[i][j])
            difference_B = current_pixel_B - int(b[0]*R[i-1][j]+b[1]*R[i][j-1]+b[2]*G[i-1][j]+b[3]*G[i][j-1]+b[4]*B[i-1][j]+b[5]*B[i][j-1]+b[6]*R[i][j]+b[7]*G[i][j])
            err_R[i, j] = uniform_quantizer(difference_R, step)
            err_G[i,j] = uniform_quantizer(difference_G, step)
            err_B[i,j]= uniform_quantizer(difference_B,step)
            current_pixel_R = err_R[i, j] + int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])  # boucle rétro
            current_pixel_G = err_G[i, j] + int(g[0]*R[i-1][j]+g[1]*R[i][j-1]+g[2]*G[i-1][j]+g[3]*G[i][j-1]+g[4]*B[i-1][j]+g[5]*B[i][j-1]+g[6]*R[i][j])
            current_pixel_B = err_B[i,j] + int(b[0]*R[i-1][j]+b[1]*R[i][j-1]+b[2]*G[i-1][j]+b[3]*G[i][j-1]+b[4]*B[i-1][j]+b[5]*B[i][j-1]+b[6]*R[i][j]+b[7]*G[i][j])
    return err_R, err_G, err_B


def my_decodeurDPCM(x, err_R, err_G, err_B, H, W):
    img = cv2.imread(x)
    R, G, B = CanauxDeCouleur(x)
    xrec_R = np.zeros((H, W), dtype=np.uint8)
    xrec_G = np.zeros((H, W), dtype=np.uint8)
    xrec_B = np.zeros((H, W), dtype=np.uint8)
    previous_pixel = 0

    for i in range(H):
        for j in range(W):
            difference_R = err_R[i, j]
            difference_G = err_G[i, j]
            difference_B = err_B[i, j]
            current_pixel_R = difference_R + int(r[0]*R[i-1][j]+r[1]*R[i][j-1]+r[2]*G[i-1][j]+r[3]*G[i][j-1]+r[4]*B[i-1][j]+r[5]*B[i][j-1])
            current_pixel_G = difference_G + int(g[0]*R[i-1][j]+g[1]*R[i][j-1]+g[2]*G[i-1][j]+g[3]*G[i][j-1]+g[4]*B[i-1][j]+g[5]*B[i][j-1]+g[6]*R[i][j])
            current_pixel_B = difference_B + int(b[0]*R[i-1][j]+b[1]*R[i][j-1]+b[2]*G[i-1][j]+b[3]*G[i][j-1]+b[4]*B[i-1][j]+b[5]*B[i][j-1]+b[6]*R[i][j]+b[7]*G[i][j])
            xrec_R[i, j] = np.clip(current_pixel_R, 0, 255)  # s'assurer que la valeur est dans [0, 255]
            xrec_G[i, j] = np.clip(current_pixel_G, 0, 255)
            xrec_B[i, j] = np.clip(current_pixel_B, 0, 255)

    return xrec_R, xrec_G, xrec_B

A,b=R(M)
r=gauss(A,b)