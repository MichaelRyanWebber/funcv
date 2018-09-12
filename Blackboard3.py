import cv2
import fof
import Diff
import Blacklines2
import Alpha

class Blackboard3:

    def __init__(self):
        self.diff = Diff.Diff()
        self.blacklines2 = Blacklines2.Blacklines2()
        self.alpha = Alpha.Alpha()

    def get_frame(self, src):
        tempc = fof.to_float(src)
        tempc = fof.blur(tempc, 15)
        tempd = cv2.cvtColor(tempc, cv2.COLOR_BGR2GRAY)
        tempd = self.diff.get_frame(tempd)
        tempd = self.blacklines2.get_frame(tempd, 60)
        tempd = fof.blur(tempd, 1)

        tempd = self.alpha.get_frame(tempd, tempc) / 255.0
        return tempd

