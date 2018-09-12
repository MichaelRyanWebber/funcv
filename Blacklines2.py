import cv2
import Trails
import fof


class Blacklines2:
    def __init__(self):
        self.trails = Trails.Trails()

    #expects 32F
    def get_frame(self, src, threshold):
        temp = fof.to_uint(src.copy())
        temp = fof.thresh(temp, threshold)
        temp = fof.contour(temp, .01, 9, 1, (255, 255, 255))

        temp = self.trails.get_frame(fof.to_float(temp), 9.0, 0.8)

        temp = temp * 10 + src

        return fof.to_float(temp)
