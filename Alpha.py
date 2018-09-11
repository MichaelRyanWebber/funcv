import cv2
import Trails
import fof


class Alpha:

    def __init__(self):
        self.trails = Trails.Trails()

    # assumes CV_32F mat
    def get_frame(self, src1, src2):
        temp = self.trails.get_frame(src1, 1.0, 0.9)
        cv2.absdiff(src1, temp, temp)
        temp = cv2.cvtColor(temp, cv2.COLOR_GRAY2BGR)
        temp = fof.squash(temp, 16, 0.1)
        # temp = cv2.multiply(temp, src2, 1. / 255)
        temp = temp * src2 / 255.0
        return temp

