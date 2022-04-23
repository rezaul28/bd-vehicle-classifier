import cv2
import os
import shutil
import sys
root =os.getcwd()
videoName = input("Enter video file name: ")
video =cv2.VideoCapture("./resource/"+videoName)
car = "./resource/car.xml"
try:
    os.remove(root+"new.mp4")
except:
    pass
try:
    shutil.rmtree(root+"photos",ignore_errors=False, onerror=None)
except:
    pass
os.mkdir(root+"photos")
car_tracker = cv2.CascadeClassifier(car)
while True:
    (read,fram) = video.read()
    if(read):
        fram = cv2.resize(fram, (300,300), interpolation = cv2.INTER_AREA)
        gray_image = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(fram)
    # buss = bus_tracker.detectMultiScale(fram)
    for (x,y,w,h) in cars:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,255))
    # for(x,y,w,h) in buss:
    #     cv2.rectangle(fram,(x,y),(x+w,y+h),(0,0,0))
    cv2.imshow("Processed image",fram)
    cv2.waitKey(1)
# print("Finished sampling")
# images = [img for img in os.listdir(img_folder) if img.endswith(".jpg")]
# print()
# def myFunc(e):
#   return int(e[:-4])
# images.sort(key=myFunc)
# frame = cv2.imread(os.path.join(img_folder, images[0]))
# height, width, layers = frame.shape
# video = cv2.VideoWriter(root+"new.mp4",int(video.get(cv2.CAP_PROP_FOURCC)) , video.get(5), (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(img_folder, image)))
# try:
#     shutil.rmtree(root+"photos",ignore_errors=False, onerror=None)
# except:
#     pass
# sys.stdout.flush()
