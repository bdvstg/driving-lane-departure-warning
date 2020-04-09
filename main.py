"""Departure Warning System with a Monocular Camera"""

__author__ = "Junsheng Fu"
__email__ = "junsheng.fu@yahoo.com"
__date__ = "March 2017"

import cv2
from lane import *

if __name__ == "__main__":

    demo = 2 # 1: image, 2 video

    if demo == 1:
        imagepath = 'examples/test3.jpg'
        img = cv2.imread(imagepath)
        img_aug = process_frame(img)

        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 9))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax1.imshow(img)
        ax1.set_title('Original Image', fontsize=30)
        img_aug = cv2.cvtColor(img_aug, cv2.COLOR_BGR2RGB)
        ax2.imshow(img_aug)
        ax2.set_title('Augmented Image', fontsize=30)
        plt.show()

    else:
        cap = cv2.VideoCapture("examples/project_video.mp4")
        while(True):
            # Capture frame-by-frame
            ret, in_frame = cap.read()
            out_frame = process_frame(in_frame)
            cv2.imshow('out_frame',out_frame)
            key = cv2.waitKey(1)
            if key == 27:
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
