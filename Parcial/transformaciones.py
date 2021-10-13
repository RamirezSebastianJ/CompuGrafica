import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def importImage(ruta_imagen):
    return cv.imread(ruta_imagen) 

def invertirImagen(ruta_imagen):
    return np.flipud(importImage(ruta_imagen))


def binarizar(image):
    gray = cv.cvtColor(importImage(image), cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum() / (w*h)
    print('mean:', mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    return binary

def zoom(ruta_imagen):
    image = importImage(ruta_imagen)
    ancho = image.shape[1] 
    alto = image.shape[0] 
    return cv.resize(image,(int(ancho*0.1),int(alto*0.1)))
    

def rotar (ruta_imagen):
    image = importImage(ruta_imagen)
    ancho = image.shape[1] 
    alto = image.shape[0] 
    M = cv.getRotationMatrix2D((ancho//2,alto//2),30,1)
    imageOut = cv.warpAffine(image,M,(ancho,alto))
    return imageOut

def cambiarBrillo(ruta_imagen, brillo):
    image = importImage(ruta_imagen)
    image[image<255-brillo]+=brillo
    return image

def cambiarContraste(ruta_imagen):
    image = importImage(ruta_imagen)
    return cv.addWeighted(image, 2.5, np.zeros(image.shape, image.dtype), 0, 0)


#################################################################################################
# Descripcion:  Función para mostrar la capa roja de una imagen.
# Llamado:  capaRoja(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa roja.
def capaRoja(Imagen):
    miImagen=plt.imread(Imagen)/255
    
    imagenRoja=np.copy(miImagen)
    imagenRoja[:,:,1]=0
    imagenRoja[:,:,2]=0

    return(imagenRoja)

#################################################################################################
# Descripcion:  Función para mostrar la capa verde de una imagen.
# Llamado:  capaVerde(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa Verde.
def capaVerde(Imagen):
    miImagen=plt.imread(Imagen)/255
    
    imagenVerde=np.copy(miImagen)
    imagenVerde[:,:,0]=0
    imagenVerde[:,:,2]=0

    return(imagenVerde)

#################################################################################################
# Descripcion:  Función para mostrar la capa Azul de una imagen.
# Llamado:  capaAzul(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa Azul.
def capaAzul(Imagen):
    miImagen=plt.imread(Imagen)/255
    
    imagenAzul=np.copy(miImagen)
    imagenAzul[:,:,0]=0
    imagenAzul[:,:,1]=0

    return(imagenAzul)

#################################################################################################
# Descripcion:  Función para mostrar la capa cian de una imagen.
# Llamado:  capaCian(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa Cian.
def capaCian(Imagen):
    miImagen=plt.imread(Imagen)/255

    imagenCian=np.copy(miImagen)
    imagenCian[:,:,1]=1
    imagenCian[:,:,2]=1

    return(imagenCian)

#################################################################################################
# Descripcion:  Función para mostrar la capa magenta de una imagen.
# Llamado:  capaMagenta(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa Magenta.
def capaMagenta(Imagen):
    miImagen=plt.imread(Imagen)/255

    imagenMagenta=np.copy(miImagen)
    imagenMagenta[:,:,0]=1
    imagenMagenta[:,:,2]=1

    return(imagenMagenta)

#################################################################################################
# Descripcion:  Función para mostrar la capa Amarilla de una imagen.
# Llamado:  capaAmarilla(Imagen).
# Parámetros:   Recibe una imagen.
# Imagen: Matriz de archivo (jpg).

# Retorna la imagen con solo su capa Amarilla.
def capaAmarilla(Imagen):
    miImagen=plt.imread(Imagen)/255

    imagenAmarilla=np.copy(miImagen)
    imagenAmarilla[:,:,0]=1
    imagenAmarilla[:,:,1]=1

    return(imagenAmarilla)