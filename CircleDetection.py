import cv2
from decimal import Decimal


def CircleDetect(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(grey, 15)
    circles = cv2.HoughCircles(blured, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=0, maxRadius=0)
    circleJSON = []
    if circles is not None:
        for i in circles[0, :]:
            circleDict = {}
            circleDict['x'] = i[0].item()
            circleDict['y'] = i[1].item()
            circleDict['radius'] = i[2].item()
            circleJSON.append(circleDict)
        return circleJSON