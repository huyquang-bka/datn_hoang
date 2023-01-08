from main_app.utils.inference_tool import InferenceTool
import time
import cv2
import imutils


infer_tool = InferenceTool()
path = "resources/Video/japanese_street.mp4"
cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    t = time.time()
    num_person = infer_tool.predict(frame)
    print("num_person: ", num_person)
    print("Time: ", time.time() - t)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break