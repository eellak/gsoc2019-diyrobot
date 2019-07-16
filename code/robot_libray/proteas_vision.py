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
	def find(self,image):
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
	def return_pos(self):
		return self.ids ,self.corners
	def detect_pos(self,ar_id):
		if len(self.ids)>0:
			if ar_id in self.ids:
				i = self.ids.index(3)
				print(self.corners[i])
				x1=self.corners[i][0][0]
				x2=self.corners[i][1][0]
				y1=self.corners[i][0][1]
				y2=self.corners[i][3][1]
				print(center_point(x1,x2,y1,y2))


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

def center_point(x1,x2,y1,y2):
	xc = ((x2-x1)/2)+x1
	yc = ((y2-y1)/2)+y1
	return int(xc),int(yc)


				

