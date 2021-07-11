from flask import Flask, request, jsonify
import sys
from time import sleep

from proteas_lib import control

app = Flask(__name__)
LOCAL_IP = '127.0.0.1'

CONTROL = None
MOTOR_A = None
MOTOR_B = None

@app.route('/')
def index():
    return 'Server for remote control of Proteas Robot is up!!'

@app.before_first_request
def before_first_request():
    global MOTOR_A, MOTOR_B
    control.start_lib()
    MOTOR_A = control.motor(17,27,22)
    MOTOR_B = control.motor(10,11,9)
    
@app.route('/shutdown')
def shutdown():
    control.clean()
    sys.exit()

@app.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        MOTOR_A.move()
        sleep(1) # Sleep for 1 second   
        MOTOR_A.stop()
        return jsonify({ "status": "ok" })

@app.route('/motor/<action>', methods=['GET'])
def motor(action):
    if request.method == 'GET':
        
        motor_name = str(request.args.get('name'))
        if motor_name == 'motor_a':
            if action == 'move': 
                MOTOR_A.move()
            elif action == 'stop':
                MOTOR_A.stop()
        elif motor_name == 'motor_b':
            if action == 'move':
                MOTOR_B.move()
            elif action == 'stop':
                MOTOR_B.stop()
        return jsonify({ "status": "ok" })


if __name__ == '__main__':
    try:
        app.run(debug=True, host=LOCAL_IP)
    finally:
        control.clean()
