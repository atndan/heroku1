import numpy as np
import cv2
from keras.models import load_model
from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def gen():
    video = cv2.VideoCapture(0)
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run()
