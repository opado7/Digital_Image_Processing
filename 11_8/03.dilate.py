import numpy as np, cv2

image = cv2.imread("../images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 오류")

mask = np.array([[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]]).astype('uint8')
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst = cv2.dilate(th_img, mask)

cv2.imshow("OpenCV dilate", dst)
cv2.waitKey(0)