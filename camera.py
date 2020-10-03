# import the necessary packages
import cv2  # defining face detector

ds_factor = 0.6


class VideoCamera(object):
    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    def get_frame(self):

        ret, frame = self.video.read()
        # frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
