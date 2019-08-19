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
				i = self.ids.index(ar_id)
				x1=self.corners[i][0][0]
				x2=self.corners[i][1][0]
				y1=self.corners[i][0][1]
				y2=self.corners[i][3][1]
				self.cx = int(((x2-x1)/2)+x1)
				self.cy = int(((y2-y1)/2)+y1)
				self.width = x2-x1
				self.height = y2-y1		
		else:
				self.cx = 0
				self.cy = 0
				self.width = 0
				self.height = 0
	def mark_frame(self,frame):
		height, width, channels = frame.shape
		cv2.line(frame,(self.cx,0),(self.cx,height),(255,0,0),1)
		cv2.line(frame,(0,self.cy),(width,self.cy),(255,0,0),1)
		return frame
	def get_pos(self):
		return self.cx,self.cy
	def get_rect(self):
		return self.width,self.height

class camera():	
	def __init__(self,camera=0):
		self.camera = camera
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
		im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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

class face_detection():
	def __init__(self):
		cascPath = '/home/pi/ext/haarcascade_frontalface_default.xml'
		self.faceCascade = cv2.CascadeClassifier(cascPath)
		self.cx = 0
		self.cy = 0
		self.width = 0
		self.height=0
		self.faces_num = 0
	def detect_face(self,frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.faceCascade.detectMultiScale(gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)
		if len(faces) > 0:
			self.faces_num = len(faces)
			(x,y,w,h)= faces[0]
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			self.cx = int(((w/2)+x))
			self.cy = int(((h/2)+y))
			self.width = w
			self.height = h
			fheight, fwidth, channels = frame.shape
			cv2.line(frame,(self.cx,0),(self.cx,fwidth),(255,0,0),1)
			cv2.line(frame,(0,self.cy),(fwidth,self.cy),(255,0,0),1)
			cv2.circle(frame,(self.cx, self.cy), 5, (0,255,0), -1)
		else:
			self.faces_num = 0
			self.cx = 0
			self.cy = 0
			self.width = 0
			self.height = 0
		return frame
	def get_faces(self):
		return self.faces_num
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
			print("Go Right")
			return 2
		elif posx >self.w2 and posx < self.width:
			print("Go Left")
			return 1
		elif posx == 0:
			print("No detection")
			return -1
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
		elif rx == 0:
			print("No detection")
			return -1
		else:
			print("Stay")
			return 0



class line_follower():
	def __init__(self,width=640,height=480,w=160,h=60):
		self.width = width
		self.height = height
		self.cx = 0
		self.cy = 0
		self.x1 = max(0,int((self.width/2) - (w/2)))
		self.x2 = min(int((self.width/2) + (w/2)),self.width)
		self.y1 = max(0,int((self.height/2) - (h/2)))
		self.y2 = min(int((self.height/2) + (h/2)),self.height)

	def detect_line(self,frame):	
		crop_img = frame[self.y1:self.y2, self.x1:self.x2]
		gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray,(5,5),0)
		ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
		contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
		if len(contours) > 0:
			c = max(contours, key=cv2.contourArea)
			M = cv2.moments(c)
			if M['m00'] != 0:
				self.cx = int(M['m10']/M['m00'])
				self.cy = int(M['m01']/M['m00'])
				cv2.line(crop_img,(self.cx,0),(self.cx,self.height),(255,0,0),1)
				cv2.line(crop_img,(0,self.cy),(self.width,self.cy),(255,0,0),1)
				cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
			else:
				self.cx = 0
				self.cy = 0
		else:
			self.cx = 0
			self.cy = 0

		return crop_img

	def get_pos(self):
		return self.cx,self.cy
