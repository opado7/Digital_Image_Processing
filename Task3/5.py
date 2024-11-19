import numpy as np, cv2

canny = cv2.imread("images/image5.jpg", cv2.IMREAD_GRAYSCALE)
if canny is None: raise Exception("파일 오류")

def on_change(pos):
    th1 = cv2.getTrackbarPos('th1', "canny")
    th2 = cv2.getTrackbarPos('th2', "canny")
    canny_img = cv2.Canny(canny, th1, th2)
    cv2.imshow("canny", canny_img)

cv2.namedWindow('canny')
cv2.createTrackbar('th1', "canny", 0, 255, on_change)
cv2.createTrackbar('th2', "canny", 0, 255, on_change)

cv2.imshow("canny", canny)
cv2.waitKey(0)