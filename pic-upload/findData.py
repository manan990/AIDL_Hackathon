from PIL import Image
import pytesseract
import re
import cv2
import numpy as np

# text = pytesseract.image_to_string(Image.open('./uploaded/6.jpg'))
dateRegEx = [
    r"([0-2][0-9]|(3)[0-1]|[0-9])(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)\d{4}",
    r"(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)([0-2][0-9]|(3)[0-1]|[0-9])(\/|\.|\-)\d{4}",
    r"(([0-9])|([0-2][0-9])|([3][0-1]))(\/|\.|\-)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|\.|\-)\d{4}",
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|July|Aug|Sep|Oct|Nov|Dec)(\/|\.|\-)(([0-9])|([0-2][0-9])|([3][0-1]))(\/|\.|\-)\d{4}",
    r"\d{4}(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)([0-2][0-9]|[0-9]|(3)[0-1])",
    r"\d{4}(\/|\.|\-)([0-2][0-9]|[0-9]|(3)[0-1])(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9])",

    r"([0-2][0-9]|(3)[0-1]|[0-9])(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)\d{2}",
    r"(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)([0-2][0-9]|(3)[0-1]|[0-9])(\/|\.|\-)\d{2}",
    r"(([0-9])|([0-2][0-9])|([3][0-1]))(\/|\.|\-)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\/|\.|\-)\d{2}",
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|July|Aug|Sep|Oct|Nov|Dec)(\/|\.|\-)(([0-9])|([0-2][0-9])|([3][0-1]))(\/|\.|\-)\d{2}",
    r"\d{2}(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9])(\/|\.|\-)([0-2][0-9]|[0-9]|(3)[0-1])",
    r"\d{2}(\/|\.|\-)([0-2][0-9]|[0-9]|(3)[0-1])(\/|\.|\-)(((0)[0-9])|((1)[0-2])|[0-9]"
]

timeRegEx = [
    r"((([0-9]{2})|([0-9])):[0-9]{2}:[0-9]{2}) (pm|am)",
    r"((([0-9]{2})|([0-9])):[0-9]{2}) (pm|am)",
    r"((([0-9]{2})|([0-9])):[0-9]{2}:[0-9]{2})",
    r"((([0-9]{2})|([0-9])):[0-9]{2})([0-9]{2}:[0-9]{2})",
    r"((([0-9]{2})|([0-9]))):[0-9]{2}"
]


def findDateAndTime(file):
    info = pytesseract.image_to_string(
        Image.open('./uploaded/{}'.format(file.filename)))
    data = {}
    x = None
    for i in dateRegEx:
        x = re.search(i, info)
        if(x):
            data['date'] = x.group()
            break

    y = None
    for j in timeRegEx:
        y = re.search(j, info)
        if(y):
            data['time'] = y.group()
            break

    return data


def remove_noise_and_smooth(img_path):
    print(img_path)
    img = cv2.imread(img_path, 0)
    filtered = cv2.adaptiveThreshold(img.astype(
        np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.erode(img, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    return thresh
