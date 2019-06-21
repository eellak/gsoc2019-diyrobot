import time
import RPi.GPIO as GPIO
import math
GPIO.setmode(GPIO.BOARD)


class buzzer():
	'''
	The buzzer class creates buzzer object. 
	e.x. buzzer_1 = buzzer(pin) by default the frequence is 1500 Hz and the duty cicle 50%.
	For custom frequence pass the frequence and the duty cicle parameter e.x. e.x. buzzer(pin,freq=1500,dc=50).
	'''
	def __init__(self,pin,freq=1500,dc=50):
		GPIO.setup(pin,GPIO.OUT)
		self.buz = GPIO.PWM(pin,freq)
		self.freq = freq
		self.dc = dc
		self.buz.start(0)
	def beep(self):
		self.buz.ChangeDutyCycle(self.dc)
		time.sleep(0.1)
		self.buz.ChangeDutyCycle(0)
	def timer(self,count):
		print("Timer start for {}".format(count))
		for i in range(1,count+1):
			self.buz.ChangeDutyCycle(self.dc)
			time.sleep(0.5)
			self.buz.ChangeDutyCycle(0)
			time.sleep(0.5)
			print("{} sec".format(i))
		print("Timer finished")

class motor():
	''' 
	The motor class create new motor objects. For every motor you should create a new object
	e.x. left_motor = motor(pwm pin,pin a ,pin b) also you can insert the frequense as freq of pwm 
	and duty cicle as dc e.x. motor(pwm pin,pin a ,pin b,freq=10000,dc=50). The dc parameter controls the speed of the motor and accepts values 0 - 100.
	By default the constructor set the frequence on 1000 HZ and the duty cicle on 50%.
	'''

	def __init__(self,speed_pin,terma_pin,termb_pin,freq=10000,dc=50):
		GPIO.setup(speed_pin,GPIO.OUT)
		GPIO.setup(terma_pin,GPIO.OUT)
		GPIO.setup(termb_pin,GPIO.OUT)
		self.terma_pin = terma_pin
		self.termb_pin = termb_pin
		self.mot = GPIO.PWM(speed_pin,freq)
		self.freq = freq
		self.dc = dc
		self.dir_control("forward")
		self.mot.start(0)
	def control_speed(self,speed):
		if speed < 0 or speed > 100:
			print("The motor speed is a percentage of total motor power. Accepted values 0-100.")
		else:
			self.mot.ChangeDutyCycle(speed)
	def set_speed(self,speed):
		if speed < 0 or speed > 100:
			print("The motor speed is a percentage of total motor power. Accepted values 0-100.")
		else:
			self.dc = speed
	def dir_control(self,direction):
		if direction == "forward":
			GPIO.output(self.terma_pin,GPIO.HIGH)
			GPIO.output(self.termb_pin,GPIO.LOW)
		elif direction == "reverse":
			GPIO.output(self.terma_pin,GPIO.LOW)
			GPIO.output(self.termb_pin,GPIO.HIGH)
		else:
			print("Motor accepts only forward and reverse values")
	def move(self,direction ="forward"):
		self.dir_control(direction)
		self.mot.ChangeDutyCycle(self.dc)
	def stop(self):
		self.mot.ChangeDutyCycle(0)

	
class odometer():
	'''
	The odometer class creates ododmeters object. 
	e.x. odometer_left = odometer(pin) by default the odometer class creates odometer object 
	with 20 step sensor disc.
	For diferent disc pass the disc parameter e.x. odometer(pin,sensor_disc = 20) 	
	'''
	def __init__(self,pin,sensor_disc = 20):
		self.pin = pin
		GPIO.setup(pin, GPIO.IN) 
		self.prev_pos = self.get_state()
		self.sensor_disc = sensor_disc
		self.steps = 0
	def get_state(self):
		return GPIO.input(self.pin)
	def count_rotations(self):
		if self.get_state():
			if not self.prev_pos:
				self.prev_pos = True
				self.steps +=1
		else:
			if self.prev_pos:
				self.prev_pos = False
				
	def get_steps(self):
		return self.steps
	def get_revolutions(self):
		return self.steps/self.sensor_disc
	def get_distance(self,wheel_diameter,precision = 2):
		circumference = wheel_diameter * math.pi
		revolutions = self.steps/self.sensor_disc
		distance = revolutions * circumference		
		return round(distance,precision)
	def reset(self):
		self.steps = 0
		
class ir_sensor():
	'''
	The ir_sensor class creates ir_sensor object for obstacle tracking. 
	e.x. left_sensor  = ir_sensor(pin)  	
	'''
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(pin, GPIO.IN) 
	def get_state(self):
		return GPIO.input(self.pin)


class ():
	'''
	The servo class creates servo object. 
	e.x. servo_1  = servo(pin)  	
	'''
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(pin,GPIO.OUT)
		self.sr_mot = GPIO.PWM(pin,50)		
		self.sr_mot.start(self.claculate_pwm(90))		
	def set_ange(self,angle):
		if angle < 0 or angle > 180 :
			print("The servo motor angle limits is between 0-180!")
		else:
			self.sr_mot.ChangeDutyCycle(self.claculate_pwm(angle))
	def claculate_pwm(self,angle):
		return (angle/18.0) + 2.5
		
		
def clean():
	'''
	This function clean up all the parameter for every gpio on RPi. 	
	'''
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)

