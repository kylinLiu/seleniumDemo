
#  pip install opencv-python
import cv2
import sys

# 人脸分类器
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 视频内容接受，一般默认是你的电脑的摄像头
video_capture = cv2.VideoCapture(0)

while True:

    # 抓取每一个视频帧数
    retval, frame = video_capture.read()

    # 转化成灰度，一边代码识别人脸
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 视频你在XML里定义的 形态， 人脸，或者驴脸，就看你的需求。
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )

    # 在抓取人脸后，画出正方形
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)

    # 展示人脸识别
    cv2.imshow('Video', frame)

    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
       sys.exit()