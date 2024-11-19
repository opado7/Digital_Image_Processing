import numpy as np, cv2

image = cv2.imread("images/image3.jpg")
if image is None: raise Exception("파일 오류")

b, g, r = cv2.split(image)

empty = np.zeros((b.shape[0],b.shape[1]), np.uint8)

blue_img = cv2.merge([b, empty, empty])

green_img = cv2.merge([empty, g, empty])

red_img = cv2.merge([empty, empty, r])

gray_b = cv2.cvtColor(blue_img, cv2.COLOR_BGR2GRAY)
gray_g = cv2.cvtColor(green_img, cv2.COLOR_BGR2GRAY)
gray_r = cv2.cvtColor(red_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray_b", gray_b)
cv2.imshow("gray_g", gray_g)
cv2.imshow("gray_r", gray_r)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)
