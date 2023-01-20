import cv2 
import numpy as np 

imageFile = './RGB_paint.png'
img = cv2.imread(imageFile)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()