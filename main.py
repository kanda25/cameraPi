import cv2
from datetime import datetime

import capture_jpg

DEV_ID = 0

WIDTH = 640
HEIGHT = 480
FPS = 5
REC_SEC = 10

def main():
    cap = cv2.VideoCapture(DEV_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.cv2_CAP_PROR_FPS, FPS)
    
    ret, frame = cap.read()
    if ret:
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = "./" + date + ".jpg"
        cv2.imwrite(path, frame)

    #key controll and video capture     
    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()