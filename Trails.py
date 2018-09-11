import cv2


class Trails:
    # this class creates "trails" by combining the src image with a running average
    def __init__(self):
        self.first = True
        self.avg = ''

    # assumes CV_32F mat as input and output
    def get_frame(self, src, gain, decay):

        if self.first:
            self.avg = src.copy() / 255
            self.first = False

        ret, self.avg = cv2.threshold(self.avg, 0.001, 255, cv2.THRESH_TOZERO)

        self.avg = (1-decay) * src / 255 + decay * self.avg

        temp = self.avg * 255

        return temp.copy()
