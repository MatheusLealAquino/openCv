import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Imagem padrao
img = cv.imread('nomefoto1.jpg',0)
img2 = img.copy()

#Imagem a ser encontrada na imagem padrao
template = cv.imread('nomefoto2.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
#methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            #'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

img = img2.copy()
method = eval('cv.TM_CCOEFF_NORMED')

# Apply template Matching
res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
    
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(template,cmap = 'gray')
plt.title('Objeto da busca'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Ponto detectado'), plt.xticks([]), plt.yticks([])
plt.suptitle('cv.TM_CCOEFF_NORMED')

plt.show()
