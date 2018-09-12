import cv2
import fof


class Trails:
    # this class creates "trails" by combining the src image with a running average
    def __init__(self):
        self.first = True
        self.avg = ''

    # assumes CV_32F mat as input and output
    def get_frame(self, src, gain, decay):

        if self.first:
            self.avg = fof.to_float(src)
            self.first = False


        ret, self.avg = cv2.threshold(self.avg, 0.001, 255, cv2.THRESH_TOZERO)

        self.avg = (1.0 - decay) * fof.to_float(src) + decay * self.avg

        #fof.to_uint(self.avg)

        return fof.to_uint(self.avg)
