import cv2
import numpy

# this file contains a set of helper functions

def to_float(src):
    dst = src.astype('float32')
    dst /= 255.0
    return dst

def to_uint(src):
    dst = src * 255
    return dst.astype('uint8')

def thresh(src, thresh_val):
    return cv2.threshold(src, thresh_val, 255, cv2.THRESH_BINARY)[1]


# Make a table based on the scale and threshold values
def squash(src, scale, thresh_val):
    #tab = numpy.empty([256, 3])
    tab = numpy.empty(256)

    for i in range(0, 255):
        x = scale * (i / 255.0 - thresh_val)
        y = (numpy.tanh(x) + 1) / 2.0
        z = y * 255
        tab[i] = z
        # tab[i, 0] = z
        # tab[i, 1] = z
        # tab[i, 2] = z

    # return to_float(cv2.LUT(to_uint(src), tab))
    return to_uint(cv2.LUT(src, tab))


def contour(src, largeness, simplicity, thickness, color):

    temp = src.copy()

    contours = cv2.findContours(temp, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
    temp = numpy.zeros_like(temp)
    # create approximate polygon (SIMPLICITY determines how approximate)
    # note, might need to cast / construct the contour into a Mat

    for i in range(len(contours)):
        c = cv2.approxPolyDP(contours[i], simplicity, 0)
        if cv2.contourArea(c) > largeness:
            # draw the qualified contour using drawContours
            cv2.drawContours(temp, contours, i, color, int(thickness)) # removed thickness

    return temp


def blur(src, size):
    return cv2.GaussianBlur(src, (size, size), 0)




