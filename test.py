import numpy as np
import cv2
import Trails
import Diff
import Wrap109
import Blacklines2
import Blackboard3
import Paint109
import fof
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('low threshold','image',0,255,nothing)
cv2.createTrackbar('high threshold','image',0,255,nothing)
# cv2.createTrackbar('kernel size','image',0,255,nothing)

trails = Trails.Trails()
trails2 = Trails.Trails()
diff = Diff.Diff()
wrap = Wrap109.Wrap109()
blacklines = Blacklines2.Blacklines2()
blackboard = Blackboard3.Blackboard3()
paint109 = Paint109.Paint109()
# blackboard3 and paint109 are the main modes

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    l = cv2.getTrackbarPos('low threshold', 'image')
    h = cv2.getTrackbarPos('high threshold', 'image')
    gray = fof.blur(gray,1)
    edges = cv2.Canny(gray, l, h)

    # new = trails.get_frame(gray, 1.0, 0.8)

    # delay = trails2.get_frame(frame, .5, .8)

    # temp = [np.float32(np.clip(i, 0, 255)) for i in new]

    # new = diff.get_frame(edges.astype('float'))

    # new = wrap.get_frame(gray, l)

    # new = blacklines.get_frame(gray, l)

    # new = blackboard.get_frame(frame)

    new = paint109.get_frame(frame)

    # new = fof.thresh(gray, l)

    # temp = cv2.convertScaleAbs(new)

    # ungray = cv2.cvtColor(temp, cv2.COLOR_GRAY2BGR)

    # new = ungray + frame/2

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    cv2.imshow('image', new)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()