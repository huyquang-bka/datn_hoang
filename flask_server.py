import time
import cv2
from flask import Flask, request, jsonify, render_template, Response
from threading import Thread
from util import predict
from queue import Queue


app = Flask(__name__, template_folder='resources/templates')

#define global variables
prediction = 0
stop = False

#define function to run in a thread
def inference(capture_queue):
    global prediction, stop
    while True:
        if stop:
            break
        if capture_queue.empty():
            time.sleep(0.001)
            continue
        img = capture_queue.get()
        print("img shape: ", img.shape)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        prediction = predict(img)

def gen():
    global stop
    stop = False
    capture_queue = Queue()
    t = Thread(target=predict, args=(capture_queue,))
    t.start()
    path="resources/Video/video.mp4"
    cap = cv2.VideoCapture(path)
    while True:
        if stop:
            break
        ret, frame = cap.read()
        if not ret:
            cap = cv2.VideoCapture(path)
            continue
        if capture_queue.empty():
            capture_queue.put(frame)
        frame = cv2.resize(frame, (640, 480))
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# define routes

@app.route('/')
def index():
    return "This is the index page"

@app.route('/get-predict', methods=['GET'])
def get_predict():
    return prediction

@app.route('/start')
def start():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop')
def stop():
    global stop, prediction
    stop = True
    prediction = 0
    return "Server stopped"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6299)