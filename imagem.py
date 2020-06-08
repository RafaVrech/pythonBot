import cv2
import numpy as np

def prepararImagem(img, upscale):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    (x, y) = img.shape
    img = cv2.resize(img, (y * upscale, x * upscale))

    img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.bilateralFilter(img, 9, 75, 75)
    img = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # cv2.imshow("a", img)
    # cv2.waitKey()

    return img
