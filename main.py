# First the code adds the Libraries Then the functions get implemented then it deploys sry I suck at commenting idiots.

# libraries
import cv2
import numpy as np
from kasa import Device
import asyncio

# variables
cam = cv2.VideoCapture(0)  # cam


# functions
async def toggle_dimmer(): #lights
    switch = await Device.connect(host="10.0.0.159")
    await switch.update()
    if switch.is_on:
        await switch.turn_off()
        print("Switch turned off")
    else:
        await switch.turn_on()
        print("Switch turned on")

def start_feed():
    show_gray = False  # Variable to toggle between color and grayscale
    show_detection = False

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if show_gray:
            cv2.imshow("Cam", gray)
        else:
            cv2.imshow("Cam", frame)

        key = cv2.waitKey(1) & 0xFF

        #color and grayscale toggle
        if key == ord('g'):
            show_gray = not show_gray
            #lights
        if key == ord('l'):
            asyncio.run(toggle_dimmer())
        #Quit
        if key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


def main():
    start_feed()

if __name__ == '__main__':
    main()