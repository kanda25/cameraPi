import cv2
from datetime import datetime

DEV_ID = 0

WIDTH = 640
HEIGHT = 480
#WIDTH = 1920
#HEIGHT = 1280
FPS = 5
REC_SEC = 10

def main():
    cap = cv2.VideoCapture(DEV_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    """
    ret, frame = cap.read()
    if ret:
        jpg_date = datetime.now().strftime("%Y%m%d_%H%M%S")
        jpg_path = "./" + jpg_date + ".jpg"
        cv2.imwrite(jpg_path, frame)
    """

    mp4_date = datetime.now().strftime("%Y%m&d_%H%M%S")
    mp4_path = mp4_date + ".mp4"
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(mp4_path, fourcc, FPS,(WIDTH, HEIGHT))
    for i in range(FPS * REC_SEC):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    #key controll and video capture     
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return 

if __name__ == "__main__":
    main()