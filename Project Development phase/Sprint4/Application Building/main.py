import cv2

video = cv2.VideoCapture(0)
print("reached - out ")
while True:
    print("reached - ")
	ret, frame = video.read()#enna pa aachu
	cv2.imshow("Frame", frame)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break

video.release()
cv2.destroyAllWindows()