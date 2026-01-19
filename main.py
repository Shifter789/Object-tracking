#libraries
import cv2
import numpy as np


#varibles
cam = cv2.VideoCapture(0) #cam

#fuctions
def start_feed():
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

def main():
    start_feed()


if __name__ == '__main__':
    main()