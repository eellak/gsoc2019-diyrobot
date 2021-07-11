from flask import Flask, request, jsonify
import sys
from time import sleep

from proteas_lib import control

app = Flask(__name__)
LOCAL_IP = '127.0.0.1'

CONTROL = None

@app.route('/')
def index():
    return 'Server for remote control of Proteas Robot is up!!'

@app.before_first_request
def before_first_request():
    control.start_lib()
    
@app.route('/shutdown')
def shutdown():
    control.clean()
    sys.exit()

if __name__ == '__main__':
    try:
        app.run(debug=True, host=LOCAL_IP)
    finally:
        control.clean()
