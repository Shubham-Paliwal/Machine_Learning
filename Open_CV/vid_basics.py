import cv2
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if ret == False:
		continue    # recapture the image

	cv2.imshow("videoframe" , frame)
	cv2.imshow("videoframe" , gray_frame)
	if cv2.waitKey(1) == 27: # escape key to exit window
		break

cap.release()
cv2.destroyAllWindows()