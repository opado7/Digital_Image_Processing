import numpy as np, cv2

image = cv2.imread("images/image4.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 오류")

pt_num = 0
pt1 = ((0, 0), (0, 0))
pt2 = list(pt1)

def click_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if param[0] == (0, 0):
            param[0] = (x, y)
            print("1번 지정 완료")
        elif param[1] == (0, 0):
            param[1] = (x, y)
            print("2번 지정 완료")
            cv2.rectangle(image, param[0], param[1], (0, 0, 0), 2)
            cv2.imshow("rectimg", image)
            hist_img = image[param[0][1]:param[1][1], param[0][0]:param[1][0]]
            hist = cv2.calcHist([hist_img], [0], None, [32], [0, 256])
            draw_hist = draw_histo(hist)
            cv2.imshow("hist", draw_hist)
            param[0] = (0, 0)
            param[1] = (0, 0)

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        cv2.rectangle(hist_img, (int(gap * i), 0), (int(gap * i + gap), int(h)), (0, 0, 0), -1)

    return cv2.flip(hist_img, 0)

cv2.imshow("image", image)
cv2.setMouseCallback('image', click_mouse, pt2)
cv2.waitKey(0)