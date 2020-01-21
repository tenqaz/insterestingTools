"""
@author: Jim
@project: interestingTools
@file: sketch.py
@time: 2020/1/20 17:21
@desc:

    将人物彩照转为素描照片
"""

import cv2


def test(img_gray):
    img_edge = cv2.adaptiveThreshold(img_gray, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, blockSize=3, C=2)
    cv2.imwrite("test1.jpg", img_edge)


def test2(img_gray):
    img_gray = cv2.medianBlur(img_gray, 5)
    img_edge = cv2.adaptiveThreshold(img_gray, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, blockSize=3, C=2)
    cv2.imwrite("test2.jpg", img_edge)


def test3(img_gray):
    img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21),
                                sigmaX=0, sigmaY=0)
    img_divide = cv2.divide(img_gray, img_blur, scale=255)
    cv2.imwrite("test3.jpg", img_divide)


def main():
    img_rgb = cv2.imread("F:\\tmp\\test4.jpg")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    test(img_gray)
    test2(img_gray)
    test3(img_gray)


if __name__ == '__main__':
    main()
