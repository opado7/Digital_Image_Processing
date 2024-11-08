import numpy as np, cv2

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = cv2.filter2D(image, -1, mask1)
    dst2 = cv2.filter2D(image, -1, mask2)

    # dst = np.clip(dst, 0, 255).astype("uint8")
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")
    return dst1, dst2

image = cv2.imread("../images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    
data1 = [-1, 0, 0,  # 수치만 바꾸면 마스크가 바뀜
          0, 1, 0,
          0, 0, 0]
data2 = [ 0, 0, -1,
          0, 1, 0,
          0, 0, 0]
dst1, dst2 = differential(image, data1, data2)  		# 회선 수행 및 두 방향의 크기 계산

cv2.imshow("image", image)
#cv2.imshow("roberts edge", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)