import cv2


#varibles
cam = cv2.VideoCapture(0) #cam

def start_feed():
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


def main():
    start_feed()


if __name__ == '__main__':
    main()