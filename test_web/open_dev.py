import cv2
import numpy as np
img = np.zeros((512,512,3), dtype = np.uint8)
cv2.line(img, (10,10), (510,510), (0, 255,0),5)