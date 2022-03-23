import cv2
import os
import shutil
import sys
root = "/home/vuzinga/Documents/Python/bd-vehicle-classifier/"
video =cv2.VideoCapture("./resource/cars.mp4")
car = "./resource/car.xml"
img_folder=root+"photos"
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
i=0
while True:
    (read,fram) = video.read()
    if(read):
        fram = cv2.resize(fram, (700,450), interpolation = cv2.INTER_AREA)
        gray_image = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(fram)
    for (x,y,w,h) in cars:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,255))
    cv2.imwrite(os.path.join( img_folder, str(i)+'.jpg'), fram) 
    i+=1
print("Finished sampling")
images = [img for img in os.listdir(img_folder) if img.endswith(".jpg")]
print()
def myFunc(e):
  return int(e[:-4])
images.sort(key=myFunc)
frame = cv2.imread(os.path.join(img_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(root+"new.mp4",int(video.get(cv2.CAP_PROP_FOURCC)) , video.get(5), (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(img_folder, image)))
try:
    shutil.rmtree(root+"photos",ignore_errors=False, onerror=None)
except:
    pass
sys.stdout.flush()
