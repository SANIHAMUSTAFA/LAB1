import matplotlib.pyplot as plt
import cv2

#RGB of HHQ
img1 = cv2.imread(r"E:\Saniha\Digital Image Processing\Alaska\HH-ALPSRP268500490-H2.2_UA.tif")
rgb1 =cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(rgb1)
plt.axis('off')
plt.title("RGB of HH")
plt.show()

#RGB of HVQ
img2 = cv2.imread(r"E:\Saniha\Digital Image Processing\Alaska\HV-ALPSRP268500490-H2.2_UA.tif")
rgb2 =cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(rgb2)
plt.axis('off')
plt.title("RGB of HV")
plt.show()