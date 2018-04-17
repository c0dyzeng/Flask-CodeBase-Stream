from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from datetime import datetime
from importlib import import_module
import camera driver
import os


# TODO:
# Check for webcam, and if not, use mock camera
if os.environ.get('CAMERA'):
    # set Camera to opencv.Camera (which should be our webcam) here
else:
    # import mock camera here


app = Flask(__name__)
bootstrap = Bootstrap(app)



visitors_list = [
    {
        'visitor_info': {'username': 'Abhi' },
        'time': '2018-04-15 12:12:26'
    }
]

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cody'}
    return render_template('index.html', title='Home', user=user)
@app.route('/visitors')
def visitors():

    return render_template('visitors.html', title='Visitors', visitors=visitors_list)
@app.route('/index', methods=['POST'])
@app.route('/', methods=['POST'])
def my_form_post():
    processed_text = request.form['text']
    visitors_list.append({"visitor_info": {"username":processed_text}, "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    return render_template('visitors.html', title='Visitors', visitors=visitors_list)




def gen(camera):
    """Video streaming generator function."""
    while True:
        # TODO: Get frame with camera.get_frame() and set to frame
        #insert code here
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/cam')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    # TODO: Return a response, by calling gen(Camera()) to get frames
    return Response( #insert code here,
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
