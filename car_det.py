import cv2

print(cv2.__version__)

cascade_src = "cars.xml"
video_src = "video1.avi"

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(img, str(len(cars)), (20, 40), 2, 1, (0, 255, 0))
    img = cv2.resize(img, (960, 540))
    cv2.imshow("video", img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
