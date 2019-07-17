import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display, HTML,clear_output
import PIL.Image

class aruco_find():
	def __init__(self):
		self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
		self.parameters =  aruco.DetectorParameters_create()
		self.ids = []
		self.corners = []
		self.cx = 0
		self.cy = 0
		self.width = 0
		self.height=0		
	def to_gray(self,image):
		return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	def detect(self,image):
		corners, ids, rejectedImgPoints = aruco.detectMarkers(image, self.aruco_dict, parameters=self.parameters)
		return corners, ids, rejectedImgPoints
	def mark_image(self,image,corners, ids):
		if ids is not None:
			self.ids = self.marks_to_list(ids)
			self.corners = self.marks_to_list(corners)
		else:
			self.ids = []
			self.corners = []
		image_marked = aruco.drawDetectedMarkers(image.copy(), corners, ids)
		return image_marked
	def detect_artifacts(self,image):
		gray = self.to_gray(image)
		corners, ids, rejectedImgPoints = self.detect(gray)
		final = self.mark_image(image,corners, ids)
		return final
	def marks_to_list(self,nplist):
		temp = []
		nplist = np.array(nplist).tolist()
		for item in nplist:
			temp.append(item[0])
		return temp
	def find(self,ar_id):
		if len(self.ids)>0:
			if ar_id in self.ids:
				i = self.ids.index(3)
				x1=self.corners[i][0][0]
				x2=self.corners[i][1][0]
				y1=self.corners[i][0][1]
				y2=self.corners[i][3][1]
				self.cx = ((x2-x1)/2)+x1
				self.cy = ((y2-y1)/2)+y1
				self.width = x2-x1
				self.height = y2-y1
		else:
				self.cx = 0
				self.cy = 0
				self.width = 0
				self.height = 0
	def get_pos(self):
		return self.cx,self.cy
	def get_rect(self):
		return self.width,self.height

class camera():	
	def __init__(self,camera=0):
		self.camera = camera		
	def start_camera(self):
		self.cap = cv2.VideoCapture(self.camera)	
	def take_frame(self):
		ret, frame = self.cap.read()
		return frame
	def stop(self):
		self.cap.release()

class show_image():
	def __init__(self,jupyter=True):
		self.jupyter = jupyter
	def cpreview(self,frame):
		cv2.imshow('frame',frame)
		cv2.waitKey(1) 
	def jpreview(self,frame):
		im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
		display(PIL.Image.fromarray(im))		
		clear_output(wait=True)	
	def preview(self,frame):
		if self.jupyter:
			self.jpreview(frame)
		else:
			self.cpreview(frame)
	def clear(self):
		if self.jupyter:	
			clear_output(wait=True)	
		else:
			cv2.destroyAllWindows()

class face_find():
	def __init__(self):
		cascPath = 'haarcascade_frontalface_default.xml'
		self.faceCascade = cv2.CascadeClassifier(cascPath)
		self.cx = 0
		self.cy = 0
		self.width = 0
		self.height=0
	def detect_face(self,frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)
		if len(faces) > 0:
			(x,y,w,h)= faces[0]
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			self.cx = int(((w/2)+x))
			self.cy = int(((h/2)+y))
			self.width = w
			self.height = h
			cv2.circle(frame,(self.cx, self.cy), 5, (0,255,0), -1)
		else:
			self.cx = 0
			self.cy = 0
			self.width = 0
			self.height = 0
		return frame
	def get_pos(self):
		return self.cx,self.cy
	def get_rect(self):
		return self.width,self.height

class robot_center():
	def __init__(self,width=640):
		self.width = width
		self.step = int(width/5)
		self.w1 = self.step*2
		self.w2 = self.step*3
		
	def direction(self,posx):
		if posx >0 and posx < self.w1:
			print("Rotate Right")
			return 2
		elif posx >self.w2 and posx < self.width:
			print("Rotate Left")
			return 1
		else:
			print("Stay")
			return 0

class robot_follow():
	def __init__(self,width=640):
		self.width = width
		self.max= int(width/2)
	def direction(self,rx):
		if rx < self.max and rx > 0:
			print("Forward")
			return 1
		elif rx > (self.max + 30):
			print("Back")
			return 2
		else:
			print("Stay")
			return 0



				

