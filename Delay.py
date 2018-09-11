import cv2

class Delay:

    def __init__(self):
        self.first = True
        self.oneTick = ''

    # assumes CV_32F mat
    def get_frame(self, src):

        if self.first:
            self.oneTick = src.copy()
            self.first = False

        ret = self.oneTick.copy()

        self.oneTick = src.copy()

        return ret
