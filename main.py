"""Departure Warning System with a Monocular Camera"""

__author__ = "Junsheng Fu"
__email__ = "junsheng.fu@yahoo.com"
__date__ = "March 2017"

import cv2
from lane import *

if __name__ == "__main__":

    cap = cv2.VideoCapture("examples/project_video.mp4")
    while(True):
        # Capture frame-by-frame
        ret, in_frame = cap.read()
        out_frame = process_frame(in_frame,True)
        cv2.imshow('out_frame',out_frame)
        key = cv2.waitKey(0)
        if key == 27:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
