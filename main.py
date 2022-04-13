import cv2
import datatime

dt_now = datatime.datatime.now()

camera = cv2.VideoCaputure(0)

while True:
    ret, frame = camera.read();
    if not ret:
        print("ret error")
        break
    
    cv2.imshow("Frame", frame)
    key = cv2.waitkey(1)#1s wait
    
    #if Esc push shut down screen
    if key = 27:
        break
    
    camera.release()
    cv2.destroyAllWindows()