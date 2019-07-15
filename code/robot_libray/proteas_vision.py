import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

class aruco_find():
	def __init__(self):
		self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
		self.parameters =  aruco.DetectorParameters_create()
	def to_gray(self,image):
		return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	def detect(self,image):
		corners, ids, rejectedImgPoints = aruco.detectMarkers(image, self.aruco_dict, parameters=self.parameters)
		return corners, ids, rejectedImgPoints
	def mark_image(self,image,corners, ids):
		image_marked = aruco.drawDetectedMarkers(image.copy(), corners, ids)
		return image_marked
	def show_image(self,image_marked,corners, ids):
		plt.figure()
		plt.imshow(image_marked)
		for i in range(len(ids)):
			c = corners[i][0]
			plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
		plt.legend()
		plt.show()

	def find(self,image):
		gray = self.to_gray(image)
		corners, ids, rejectedImgPoints = self.detect(gray)
		final = self.mark_image(image,corners, ids)
		return final


class camera():
	def __init__(self,cam=0):
		self.cap = cv2.VideoCapture(cam)
	def take_frame(self):
		ret, frame = self.cap.read()
		return frame
	def preview(self,frame):
		cv2.imshow('frame',frame)
		cv2.waitKey(1) 

	def stop(self):
		self.cap.release()
		cv2.destroyAllWindows()


