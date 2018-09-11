import cv2
import Delay
import Trails


class Diff:

    def __init__(self):
        self.first = True
        self.delay = Delay.Delay()
        self.trails = Trails.Trails()

    # assumes CV_32F mat
    def get_frame(self, src):
        temp = src.copy()
        temp = self.delay.get_frame(temp)
        temp = self.trails.get_frame(temp, 1.0, 0.95)

        cv2.absdiff(src, temp, temp)
        return temp
