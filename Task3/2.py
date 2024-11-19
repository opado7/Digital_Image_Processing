import numpy as np, cv2

image = cv2.imread("images/image2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 오류")

def click_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        hist1 = cv2.equalizeHist(image)

        start_dot = (x - 50, y - 50)
        end_dot = (x + 50, y + 50)

        hist_img = np.zeros((100, 100), np.uint8)

        for i in range(100):
            for j in range(100):
                hist_img[i, j] = hist1[i + start_dot[1], j + start_dot[0]]

        for i in range(100):
            for j in range(100):
                image[i + start_dot[1], j + start_dot[0]] = hist_img[i, j]

        cv2.imshow("hist_img", image)

cv2.imshow("image", image)
cv2.setMouseCallback("image", click_mouse)
cv2.waitKey(0)