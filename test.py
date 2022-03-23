import cv2
video =cv2.VideoCapture("./resource/cars.mp4")
car = "./resource/car.xml"
car_tracker = cv2.CascadeClassifier(car)
fram= cv2.imread("./resource/bicycle (2).jpg")
height, width, channels = fram.shape
print(height,width)
cars= [[464,102,26,60],[427,112,37,70],[328,126,54,91],[164,178,144,140],[2,154,178,157]]
for (x,y,w,h) in cars:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,255))
cv2.imshow("Processed image",fram)
cv2.waitKey()