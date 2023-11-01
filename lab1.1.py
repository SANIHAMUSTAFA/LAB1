from rasterio.plot import show
from PIL import Image


# reading tiff file
img1 = Image.open(r"E:\Saniha\Digital Image Processing\Alaska\HH-ALPSRP268500490-H2.2_UA.tif")
img2 = Image.open(r"E:\Saniha\Digital Image Processing\Alaska\HV-ALPSRP268500490-H2.2_UA.tif")
show(img1)
pixels = img1.load()
show(img2)
pixels = img2.load()