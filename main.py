import time
import cv2
import numpy as np
import math
from MotorAction import MotorAction

def main():
    motor = MotorAction()
    theta = 0
    minLineLength = 5
    maxLineGap = 10
    motor.initDCMotor()
    cap = cv2.VideoCapture(0)
    while True:

        ret, image = cap.read()

        if ret:
            imgHeight = image.shape[0]
            imgWidth = image.shape[1]
            image= image[int(imgHeight-imgHeight/7):int(imgHeight), 0:imgWidth]
            grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(grayColor, (5, 5), 0)
            edge = cv2.Canny(blurred, 85, 85)
            detectedLines = cv2.HoughLinesP(edge, 1, np.pi/180, 10, minLineLength, maxLineGap)
            if(lines is not None):
                for i in range(0, len(detectedLines)):
                    for x1, y1, x2, y2 in detectedLines[i]:
                        cv2.line(image,(x1,y1),(x2,y2),(0,260,0),2)
                        theta = theta+math.atan2((y2-y1), (x2-x1))
            if(theta>-2 and theta<0.6):
                motor.goForward(speed=30)
            elif(theta>0.6):
                motor.goLeft()
            elif(theta<=-2):
                motor.goRight()
            theta = 0
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()