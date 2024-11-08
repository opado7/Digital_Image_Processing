import numpy as np, cv2

image = cv2.imread("../images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

canny2 = cv2.Canny(image, 100, 150)                 # OpenCV 캐니 에지
canny3 = cv2.Canny(image, 50, 256)

cv2.imshow("image", image)           # 사용자 정의 캐니
cv2.imshow("OpenCV_Canny", canny2)           # OpenCV 캐니 에지
cv2.imshow("OpenCV_Canny2", canny3)
cv2.waitKey(0)