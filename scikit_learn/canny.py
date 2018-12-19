import cv2

img = cv2.imread("eraser2.jpeg",0)
img_canny = cv2.Canny(img, 10, 180)
cv2.imshow("Canny",img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_canny = cv2.Canny(img, 100, 1074)
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
