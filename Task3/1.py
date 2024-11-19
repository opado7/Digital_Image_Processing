import numpy as np, cv2

image = cv2.imread("images/image1.jpg")
if image is None: raise Exception("파일 오류")

size = np.array([image.shape[1], image.shape[0]])

resize_img = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)

def click_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size[0] = size[0] - size[0] // 10
        size[1] = size[1] - size[1] // 10
        resize_img = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('image', resize_img)
        return
    elif event == cv2.EVENT_RBUTTONDOWN:
        size[0] = size[0] + size[0] // 10
        size[1] = size[1] + size[1] //10
        resize_img = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('image', resize_img)
        return


cv2.imshow('image', resize_img)
cv2.setMouseCallback('image', click_mouse)
cv2.waitKey(0)