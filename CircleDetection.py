import cv2
import time
import math
import numpy as np


def CircleDetect(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(grey, 15)
    circles = cv2.HoughCircles(blured, cv2.HOUGH_GRADIENT, 1, 20, param1=70, param2=50, minRadius=0, maxRadius=0)
    circleJSON = []
    if circles is not None:
        for i in circles[0, :]:
            circleDict = {}
            circleDict['x'] = i[0]
            circleDict['y'] = i[1]
            circleDict['radius'] = i[2]
            circleJSON.append(circleDict)
            print 'x:{}, y:{}, radius: {}'.format(i[0], i[1], i[2])
        return circleJSON