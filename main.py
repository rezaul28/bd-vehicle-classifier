import cv2
video =cv2.VideoCapture("./resource/cars.mp4")
car = "./resource/car.xml"
car_tracker = cv2.CascadeClassifier(car)
while True:
    (read,fram) = video.read()
    if(read):
        gray_image = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(fram)
    print(cars)
    for (x,y,w,h) in cars:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,255))
    cv2.imshow("Processed image",fram)
    cv2.waitKey(1)
