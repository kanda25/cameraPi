import cv2
from datetime import datetime

DEV_ID = 0

WIDTH = 640
HEIGHT = 480

def main():
    cap = cv2.VideoCapture(DEV_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    ret, frame = cap.read()
    if ret:
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = "./" + date + ".jpg"
        cv2.imwrite(path, frame)
    
    cap.release()
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    main()