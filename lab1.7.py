import matplotlib.pyplot as plt

import cv2
#canny edge detection of HHQ
try:
    img1 = cv2.imread(r"E:\Saniha\Digital Image Processing\Alaska\HH-ALPSRP268500490-H2.2_UA.tif")
    edge1 = cv2.Canny(img1, 15, 10)
    cv2.imwrite("Canny Edge of HH.tiff", edge1)
    plt.imshow(edge1)
    plt.title("Canny Edge")
    plt.show()
except IOError:
    print("Error")

#canny edge detection of HVQ
try:
    img2 = cv2.imread(r"E:\Saniha\Digital Image Processing\Alaska\HV-ALPSRP268500490-H2.2_UA.tif")
    edge2 = cv2.Canny(img2, 15, 10)
    cv2.imwrite("Canny Edge of HV.tiff", edge2)
    plt.imshow(edge2)
    plt.title("Canny Edge")
    plt.show()
except IOError:
    print("Error")