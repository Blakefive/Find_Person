import cv2
import random

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread("image4.jpg")
n = 0

detected, _ = hog.detectMultiScale(img)  # 사각형 정보를 받아옴

for (x, y, w, h) in detected:
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.rectangle(img, (x, y, w, h), c, 3)
    cv2.circle(img, (int((x*2 + w)/2), int((y*2 + h)/2)), 3, (0, 0, 255), -1)
    n += 1
    print("사람",n)
    print("사람 영역 좌표:",x, y, x + w, y + h)
    print("사람 영역 중심 좌표:", int((x*2 + w)/2), int((y*2 + h)/2))
    print("원점과의 거리:",abs(int(img.shape[1]/2)- int((x*2 + w)/2)), abs(int(img.shape[0]/2) - int((y*2 + h)/2)))
    print("========================================================")

cv2.circle(img, (int(img.shape[1]/2), int(img.shape[0]/2)), 5, (255, 0, 0), -1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()