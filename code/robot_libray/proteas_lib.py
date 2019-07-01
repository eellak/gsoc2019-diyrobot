import time
import RPi.GPIO as GPIO
import math
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import ImageFont,ImageDraw,Image
from netifaces import interfaces, ifaddresses, AF_INET

class screen():
	def __init__(self,SCLK = 21,DIN = 20,DC = 16,RST =7,CS = 12):
		self.SCLK = SCLK
		self.DIN = DIN
		self.DC = DC
		self.RST = RST
		self.CS = CS
		self.disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
		self.disp.begin(contrast=60)
		self.font = ImageFont.load_default() #ImageFont.truetype('Minecraftia.ttf', 8)
		self.clear_scrn()
		self.empty_canvas()

	def clear_scrn(self):
		self.disp.clear()
		self.disp.display()
	def empty_canvas(self):
		self.canvas= Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
		self.draw = ImageDraw.Draw(self.canvas)
		self.draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

	def show_text(self,text,x=0,y=0):
		self.draw.text((x,y),text, font=self.font)

	def show_canvas(self):
		self.disp.image(self.canvas)
		self.disp.display()
	def ip_screen(self):
		self.clear_scrn()
		self.empty_canvas()
		self.show_text("Proteas Robot")
		ipl = get_ip()
		self.show_text("Connect to:",0,9)
		self.show_text("http://",0,19)
		self.show_text(ipl[-1],0,29)
		self.show_text(":8080",0,39)
		self.show_canvas()
		
	def print_text(self,text_list):
		self.clear_scrn()
		self.empty_canvas()
		posy = 0
		for i in range(0,5):	
			temp  = text_list[i]
			if isinstance(temp,int) or isinstance(temp,float):
				temp = str(temp)
			self.show_text(temp,0,posy)
			posy += 9
		self.show_canvas()
	def show_image(self,path):
		path = "images/" +path		
		self.clear_scrn()
		im = Image.open(path)
		self.canvas = im.resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
		self.show_canvas()
	
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


class servo ():
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

def start_lib():
	GPIO.setmode(GPIO.BCM)
	
	
def get_ip():
	ip_list = []
	for ifaceName in interfaces():
		addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
		print(addresses[0])
		ip_list.append(addresses[0])
	return ip_list		
		
def clean():
	'''
	This function clean up all the parameter for every gpio on RPi. 	
	'''
	GPIO.cleanup()


