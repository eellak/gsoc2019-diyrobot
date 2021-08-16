from flask import Flask, request, jsonify
import sys
from time import sleep

from proteas_lib import control
from flask import send_file

app = Flask(__name__)
LOCAL_IP = '127.0.0.1'

CONTROL = None
MOTOR_A = None
MOTOR_B = None
ODOMETER_A = None # attached to right wheel 
ODOMETER_B = None 
ULTRA_OBS = None

STATE = {
    'motor_a': 'stop', # 3 choices of direction of movement: move, stop, reverse
    'motor_b': 'stop'
}

@app.route('/')
def index():
    return 'Server for remote control of Proteas Robot is up!!'

@app.before_first_request
def before_first_request():
    global MOTOR_A, MOTOR_B, ODOMETER_A, ODOMETER_B, ULTRA_OBS
    control.start_lib()
    MOTOR_A = control.motor(17,27,22)
    MOTOR_B = control.motor(10,11,9)
    ODOMETER_A = control.odometer(6)
    ODOMETER_B = control.odometer(13)
    ULTRA_OBS = control.ultrasonic_sensor()
    
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
        
@app.route('/dist', methods=['GET'])
def dist():
    if request.method == 'GET':
        dist_u = ULTRA_OBS.get_distance()
        return jsonify({ 
            "status": "ok",
            "dist_u": dist_u  
        })
        

@app.route('/odometer/<action>', methods=['GET'])
def odometer(action):
    if request.method == 'GET':
        if action == 'reset':
            ODOMETER_A.reset()
            ODOMETER_B.reset()
            return jsonify({ "status": "ok" })
        elif action == 'dist':
            dist_a = ODOMETER_A.get_distance()
            dist_b = ODOMETER_B.get_distance()
            return jsonify({ 
                "status": "ok",
                "dist_a": dist_a, 
                "dist_b": dist_b 
            })
        elif action == 'rev':
            rev_a = ODOMETER_A.get_revolutions()
            rev_b = ODOMETER_B.get_revolutions()
            return jsonify({ 
                "status": "ok",
                "rev_a": rev_a,
                "rev_b": rev_b                 
            })
        else:
            print('ERROR')
            return jsonify({ "status": "error in flask server (unmet condition)" })



@app.route('/motor/<action>', methods=['GET'])
def motor(action):
    if request.method == 'GET':
        motor_name = str(request.args.get('name'))
        if motor_name == 'motor_a':
            if action == 'move': 
                MOTOR_A.move()
                STATE['motor_a'] = 'move'
            elif action == 'reverse':
                MOTOR_A.move("reverse")
                STATE['motor_a'] = 'reverse'
            elif action == 'stop':
                MOTOR_A.stop()
                STATE['motor_a'] = 'stop'
        elif motor_name == 'motor_b':
            if action == 'move':
                MOTOR_B.move()
                STATE['motor_b'] = 'move'
            elif action == 'reverse':
                MOTOR_B.move("reverse")
                STATE['motor_b'] = 'reverse'
            elif action == 'stop':
                MOTOR_B.stop()
                STATE['motor_b'] = 'stop'
        return jsonify({ "status": "ok" })
        

@app.route('/state', methods=['GET'])
def state():
    if request.method == 'GET':
        dist_a = ODOMETER_A.get_distance()
        dist_b = ODOMETER_B.get_distance()
        rev_a = ODOMETER_A.get_revolutions()
        rev_b = ODOMETER_B.get_revolutions()
        dist_u = ULTRA_OBS.get_distance()
        motor_a = STATE['motor_a']
        motor_b = STATE['motor_b']
        return jsonify({ 
            "status": "ok",
            "dist_a": dist_a, 
            "dist_b": dist_b,
            "rev_a": rev_a,
            "rev_b": rev_b,
            "dist_u": dist_u,
            "motor_a": motor_a,
            "motor_b": motor_b
        })

@app.route('/route', methods=['GET'])
def route():
    if request.method == 'GET':
        if True: # TODO
            filename = '../node-red/robot_state/route.png'
        else:
            filename = '../node-red/robot_state/error.png'
        return send_file(filename, mimetype='image/png')
        # return jsonify({ "status": "ok" })

# ~ @app.route('/motors/<action>', methods=['GET'])
# ~ def motor(action):
    # ~ if request.method == 'GET':
        # ~ if action == 'set':
        
        # ~ elif action == 'move':
            # ~ motor_name = str(request.args.get('name'))
            # ~ if motor_name == 'motor_a':
                # ~ MOTOR_A.move()
            # ~ elif motor_name == 'motor_b':
                # ~ MOTOR_B.move()
            # ~ else:
                # ~ print('ERROR (in moving given motor)')
        # ~ elif action == 'stop':
            # ~ motor_name = str(request.args.get('name'))
            # ~ if motor_name == 'motor_a':
                # ~ MOTOR_A.stop()
            # ~ elif motor_name == 'motor_b':
                # ~ MOTOR_B.stop()
            # ~ else:
                # ~ print('ERROR (in stopping given motor)')
        # ~ else:
            # ~ print('ERROR (in motors endpoint http request)')
        # ~ return jsonify({ "status": "ok" })

@app.route('/motor_set', methods=['GET'])
def motor_set():
    global MOTOR_A, MOTOR_B, ULTRA_OBS
    if request.method == 'GET':
        # ~ control.clean()
        # ~ control.start_lib()
        motor_a_en = int(request.args.get('motor_a_en'))
        motor_a_in1 = int(request.args.get('motor_a_in1'))
        motor_a_in2 = int(request.args.get('motor_a_in2'))
        motor_b_en = int(request.args.get('motor_b_en'))
        motor_b_in1 = int(request.args.get('motor_b_in1'))
        motor_b_in2 = int(request.args.get('motor_b_in2'))
        # ~ MOTOR_A = control.motor(motor_a_en,motor_a_in1,motor_a_in2)
        # ~ MOTOR_B = control.motor(motor_b_en,motor_b_in1,motor_b_in2)
        # ~ ULTRA_OBS = control.ultrasonic_sensor()
        return jsonify({ "status": "ok" })
# ~ /motor_set?motor_a_en=17&motor_a_in1=27&motor_a_in2=22&motor_b_en=10&motor_b_in1=11&motor_b_in2=9

if __name__ == '__main__':
    try:
        app.run(debug=True, host=LOCAL_IP)
    finally:
        control.clean()
