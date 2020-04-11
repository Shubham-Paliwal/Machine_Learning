import cv2 as cv
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface.xml")
while True:
	ret, frame = cap.read()
	g_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	if ret == False:
		continue
	faces = face_cascade.detectMultiScale(g_frame, 1.3, 5)
	# tuple of (x, y, w, h). (x, y) - leftmost coordinate. length. ht
	for (x, y, w, h) in faces:
		cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
	cv.imshow("Stream, Say Cheese!", frame)
	if cv.waitKey(1) == 27:
		break
cap.release()
cv.destroyAllWindows()