from cv2 import *

IMG_SRC = 'C:/Users/ACER/Desktop/Thesis/src.png'

if __name__ == '__main__':
    src = imread(IMG_SRC)

    # Kernel definition
    kernel = getStructuringElement(MORPH_ELLIPSE, (20, 20))

    # Contrast enhancement
    dilated = dilate(src, kernel)
    topHat = morphologyEx(src, MORPH_TOPHAT, kernel)
    blackHat = morphologyEx(src, MORPH_BLACKHAT, kernel)
    accentuated = add(src, topHat)
    highContrast = subtract(accentuated, blackHat)

    # Background subtraction
    backgroundSubtraction = subtract(highContrast, dilated)

    # Threshold to extract microcalcifications
    th, thresholding = threshold(backgroundSubtraction, 25, 255, THRESH_BINARY)
 
    imshow("Original Image",src)
    imshow('Microcalcifications', thresholding)
    waitKey(0)