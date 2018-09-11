import cv2

class Delay:
    # this class defines a one frame delay
    # i.e. it returns the frame it was passed the last time it was called
    def __init__(self):
        self.first = True
        self.oneTick = ''

    # assumes CV_32F mat as input and output
    def get_frame(self, src):

        if self.first:
            self.oneTick = src.copy()
            self.first = False

        ret = self.oneTick.copy()

        self.oneTick = src.copy()

        return ret
