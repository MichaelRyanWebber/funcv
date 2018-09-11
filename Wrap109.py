import cv2
import Trails
import fof


class Wrap109:

    def __init__(self):
        self.trails = Trails.Trails()

    # assumes CV_32F mat
    def get_frame(self, src, threshold):
        temp = src.astype('uint8').copy()
        temp = fof.thresh(temp, threshold)
        temp = fof.contour(temp, .01, 9, 1.5, (255, 255, 255))

        temp = self.trails.get_frame(temp.astype('float32'), 9.0, 0.8)

        temp = 2 * temp + .6 * src
        return temp

