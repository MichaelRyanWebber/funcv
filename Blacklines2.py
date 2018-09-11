import cv2
import Trails
import fof


class Blacklines2:
    def __init__(self):
        self.trails = Trails.Trails()

    def get_frame(self, src, threshold):
        temp = src.copy()
        temp = fof.thresh(temp, threshold)
        temp = fof.contour(temp, .01, 9, 1, (255, 255, 255))

        temp = self.trails.get_frame(temp, 9.0, 0.8)

        temp = temp * 10 + src

        return temp
