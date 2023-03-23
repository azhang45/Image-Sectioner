from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
from scipy import ndimage

pic = plt.imread('OneDrive/personal-projects/Image-Sectioner/images/PCAM3.png')/255
print(pic.shape)
plt.imshow(pic)