import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt

from transformaciones import *


def basicas():
    width=5
    height=5
    rows = 2
    cols = 3
    axes=[]
    axes2=[]
    img = cv.imread('./gatos-gestos-m.jpg')
    fig=plt.figure('Transformaciones básicas de una imagen')
    flip_up = np.flipud(img)


    axes.append( fig.add_subplot(rows, cols, 1) )
    subplot_title=("Imagen Original")
    axes[-1].set_title(subplot_title)
    plt.imshow(importImage('./gatos-gestos-m.jpg'))

    axes.append( fig.add_subplot(rows, cols, 2) )
    subplot_title=("Imagen con brillo alterado")
    axes[-1].set_title(subplot_title)
    plt.imshow(cambiarBrillo('./gatos-gestos-m.jpg', 40))

    axes.append( fig.add_subplot(rows, cols, 3) )
    subplot_title=("Imagen con contraset alterado")
    axes[-1].set_title(subplot_title)
    plt.imshow(cambiarContraste('./gatos-gestos-m.jpg'))

    fig.tight_layout()
    plt.show()

def digitales():
    width=5
    height=5
    rows = 2
    cols = 3
    axes=[]
    axes2=[]
    img = cv.imread('./gatos-gestos-m.jpg')
    fig=plt.figure('Tratamiento digital una imagen')
    flip_up = np.flipud(img)


    axes.append( fig.add_subplot(rows, cols, 1) )
    subplot_title=("Imagen Original")
    axes[-1].set_title(subplot_title)
    plt.imshow(importImage('./gatos-gestos-m.jpg'))

    axes.append( fig.add_subplot(rows, cols, 2) )
    subplot_title=("Imagen Invertida")
    axes[-1].set_title(subplot_title)
    plt.imshow(invertirImagen('./gatos-gestos-m.jpg'))

    axes.append( fig.add_subplot(rows, cols, 3) )
    subplot_title=("Imagen Binarizada")
    axes[-1].set_title(subplot_title)
    plt.imshow(binarizar('./gatos-gestos-m.jpg'))

    axes.append( fig.add_subplot(rows, cols, 4) )
    subplot_title=("Imagen con zoom")
    axes[-1].set_title(subplot_title)
    plt.imshow(zoom('./gatos-gestos-m.jpg'))

    axes.append( fig.add_subplot(rows, cols, 5) )
    subplot_title=("Imagen con zoom")
    axes[-1].set_title(subplot_title)
    plt.imshow(rotar('./gatos-gestos-m.jpg'))


    fig.tight_layout()
    plt.show()

def rgb_cmyk(imagen):

    plt.figure('Capas RGB y CMYK de una imagen')
    plt.subplot(2,3,1)
    plt.title('imagen Roja')
    imagenRoja=capaRoja(imagen)
    print(imagenRoja)
    plt.imshow(imagenRoja)

    plt.subplot(2,3,2)
    plt.title('imagen Verde')
    imagenVerde=capaVerde(imagen)
    plt.imshow(imagenVerde)

    plt.subplot(2,3,3)
    plt.title('imagen Azul')
    imagenAzul=capaAzul(imagen)
    plt.imshow(imagenAzul)
    
    plt.subplot(2,3,4)
    plt.title('imagen Cian')
    imagenCian=capaCian(imagen)
    plt.imshow(imagenCian)

    plt.subplot(2,3,5)
    plt.title('imagen Magenta')
    imagenMagenta=capaMagenta(imagen)
    plt.imshow(imagenMagenta)

    plt.subplot(2,3,6)
    plt.title('imagen Amarilla')
    imagenAmarilla=capaAmarilla(imagen)
    plt.imshow(imagenAmarilla)

    plt.show()



basicas()
digitales()
rgb_cmyk('./gatos-gestos-m.jpg')
