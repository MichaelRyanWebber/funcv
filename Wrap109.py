import cv2
import Trails
import fof


class Wrap109:

    def __init__(self):
        self.trails = Trails.Trails()

    def get_frame(self, src, threshold):
        temp = src.copy()
        temp = fof.thresh(temp, threshold)
        temp = fof.contour(temp, .01, 9, 1.5, (255, 255, 255))

        temp = self.trails.get_frame(temp, 9.0, 0.8)

        temp = 2 * fof.to_float(temp) + fof.to_float(src) * .6
        return fof.to_uint(temp)

