import cv2
import fof
import Diff
import Trails
import Wrap109
import numpy


class Paint109:

    def __init__(self):
        self.diff1 = Diff.Diff()
        self.diff2 = Diff.Diff()
        self.trails = Trails.Trails()
        self.wrap109 = Wrap109.Wrap109()

    def get_frame(self, src):

        #tempc = fof.to_float(src)
        tempc = src
        tempc = cv2.cvtColor(tempc, cv2.COLOR_BGR2GRAY)
        tempc = fof.to_uint(fof.to_float(tempc) * 1.5)
        tempc = self.diff1.get_frame(tempc)

        tempc = fof.thresh(tempc, 50)

        tempc = fof.blur(tempc, 5)

        #temp1 = cv2.cvtColor(tempc, cv2.COLOR_GRAY2BGR)
        temp1 = fof.squash(tempc, 12.0, 0.9)
        # temp1 = cv2.cvtColor
        # temp1 = tempc
        temp1 = self.diff2.get_frame(temp1)
        temp1 *= 5
        temp1 = self.trails.get_frame(temp1, 9.0, .9)

        temp2 = cv2.bitwise_not(tempc)
        temp2 = self.wrap109.get_frame(temp2, 225)
        temp2 = cv2.bitwise_not(temp2)


        dst = 0.8 * fof.to_float(temp1) + 0.6 * fof.to_float(temp2)

        # dst = cv2.cvtColor(dst.astype('float32'), cv2.COLOR_GRAY2BGR)
        # dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)


        return fof.to_uint(dst)


