from PIL import Image
from skimage.morphology import thin, skeletonize
import matplotlib.pyplot as plt
import cv2
from numpy import *
import numpy as np
import scipy.ndimage
import math
img1 = cv2.imread('1.bmp', 0)
ret, th1 = cv2.threshold(img1, 240, 255, cv2.THRESH_BINARY)
imgbw = ~th1
imgbw2 = imgbw/255
skeli = skeletonize(imgbw2)
skeli = skeli.astype(np.uint8)

itemindexrow, itemindexcolumn = np.where(skeli == 1)
minrow = min(itemindexrow)
maxrow = max(itemindexrow)
mincolumn = min(itemindexcolumn)
maxcolumn = max(itemindexcolumn)

croppedimage = skeli[minrow:maxrow, mincolumn:maxcolumn]

#width-to -height
newrow = maxrow - minrow
newcolumn = maxcolumn - mincolumn
ratio = newcolumn / newrow

#Signature-intensity
sumOfpixels = np.sum(sum(skeli))
hole = newrow * newcolumn
intensity = sumOfpixels / hole

# maximum projection in vetical and horizontal axis
verticalsum = [sum(skeli[i]) for i in range(200)]
horizentalsum = [sum(skeli[:, i]) for i in range(200)]
maxvertical = max(verticalsum)
maxhorizontal = max(horizentalsum)
step =10
positionv = math.ceil(maxvertical / step)
positionh= math.ceil(maxhorizontal / step)







