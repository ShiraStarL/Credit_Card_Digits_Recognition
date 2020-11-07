import cv2
import numpy as np


def preprocess(img, debug=True):

    # image dimensions
    height, width = img.shape[:2]

    # crop image as card rectangle
    a = int(height * 0.125)
    b = int(width * 0.406)
    x1 = int(width/2) - b
    x2 = int(width/2) + b
    y1 = int(height/2) - a
    y2 = int(height/2) + a
    img = img[y1:y2, x1:x2].copy()

    height, width = img.shape[:2]
    img_size = height*width

    # convert RGB to Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold for binary image (black and white)
    ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # clean noise in background
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # find all contours in image
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if debug:
        # draw all contours
        counts = img.copy()
        cv2.drawContours(counts, contours, -1, (0, 255, 0), 3)

    # find the biggest contour (c) by the area
    c = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)

    if debug:
        # draw rectangle around contour
        card_rect = img.copy()
        cv2.rectangle(card_rect, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # check if the bigger counter is the credit card by calculate the percentage of it from the all image
    per = (h*w)/img_size
    if per > 0.5:
        card_image = img[y:y+h, x:x+w].copy()
        if debug:
            cv2.imwrite("debug/card_image.jpg", card_image)
        return card_image
    else:
        return img

