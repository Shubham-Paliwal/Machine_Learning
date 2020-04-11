import cv2
import matplotlib.pyplot as plt
# reading the image
# open cv reads image by default as BGR
img = cv2.imread('snape.jpg')
new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(new_img)
# plt.show()

# ---------------Showing image using opencv------------------

gray = cv2.imread('snape.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Snape!', img)
cv2.imshow('Gray snape', gray)
cv2.waitKey(0) # (t) miliseconds for which image is being displayed
cv2.destroyWindow()


