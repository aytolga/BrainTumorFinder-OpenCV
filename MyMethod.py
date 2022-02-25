"""

The brain tumor finder function for MR images including some
steps from Image Processing.

Author: Tolga AY
Github: evnflow3
Mail: ecetolgaay@gmail.com

"""
import cv2            #Implenetaion of OpenCV Library.

def TumorFinder(img,g1,g2,th):       #Definition of the function.
    """


    :param img: The image upload image for finder.
    :param g1: Gaussian filter parameter, choose odd numbers for blurring, higher numbers gets higher blur.
    :param g2: Gaussian filter parameter, choose odd numbers for blurring, higher numbers gets higher blur.
    :param th: Threshold value for finding the exact area.

    
    """

    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            #Taking the image from the parameter and turning It to the gray scale.
    cv2.imshow("Picture", gray)

    masked = cv2.GaussianBlur(gray, (0, 0), g1, g2)         #Gaussian filter for blurring and reducing noise.
    cv2.imshow("Blur", masked)

    threshold, thresh = cv2.threshold(masked, th, 255, cv2.THRESH_BINARY)        #Threshold method with binary for exact tumor area.
    cv2.imshow("Thresh", thresh)

    canny = cv2.Canny(thresh, th, 255)              #Canny edge detection for edges.
    cv2.imshow("Canny",canny)

    x, y, w, h = cv2.boundingRect(canny)
    final = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)      #Bounding for tumor area.

    cv2.imshow("The Tumor Area", final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
