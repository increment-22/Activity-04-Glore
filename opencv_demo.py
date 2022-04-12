import cv2
filePath = 'GLORE_SMILEY.jpg'
image = cv2.imread(filePath, 1)
cv2.imshow("Smiley", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
