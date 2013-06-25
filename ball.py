import numpy as np
import time

FRICTION = 0.9
G = 9.8

class Ball:
	vel = 0.0
	t = 0.0
	heading = 0.0
	
	def __init__(self, type, color, number, xpos, ypos):
		self.type = type
		self.color = color
		self.number = number
		self.xpos = xpos
		self.ypos = ypos
		self.inmotion = 0
		self.u = 0.0

	def collideBall(self, v, angle, xoffset, yoffset):
		#Record current details
		cur_time = time.time()
		self.xpos, self.ypos = self.currentPos(cur_time)
		self.u = self.vel

		#Start new heading
		x = self.currentVel(cur_time)*np.cos(self.heading) + v*np.cos(angle)
		y = self.currentVel(cur_time)*np.sin(self.heading) + v*np.sin(angle)
		self.vel = np.sqrt(x*x + y*y)
		self.heading = np.arctan(y/x)

		#Set into motion
		self.inmotion = 1

		#Start next timer
		self.t = cur_time

	def isMoving(self, cur_time):
		elapsed_time = cur_time-self.t
		if elapsed_time <= self.vel/(FRICTION*G):
			return True
		else:
			self.inmotion = 0
			self.xpos = self.xpos + np.cos(self.heading)*np.square(self.vel)/(2*FRICTION*G)
			self.ypos = self.ypos + np.sin(self.heading)*np.square(self.vel)/(2*FRICTION*G)
			self.vel = 0
			self.u = 0
			return False

	def currentVel(self, cur_time):
		elapsed_time = cur_time-self.t
		if self.isMoving(cur_time):
			cur_vel = self.vel - FRICTION*G*elapsed_time
		else:
			cur_vel = 0
		return cur_vel
	
	def currentPos(self, cur_time):
		elapsed_time = cur_time-self.t
		if self.isMoving(cur_time):
			#d = (np.square(self.currentVel(cur_time)) - np.square(self.vel))/(-2*FRICTION*G)
			d = -0.5*FRICTION*G*np.square(elapsed_time) + self.vel*elapsed_time
			cur_xpos = self.xpos + d*np.cos(self.heading)
			cur_ypos = self.ypos + d*np.sin(self.heading)
		else:
			cur_xpos = self.xpos
			cur_ypos = self.ypos

		return cur_xpos, cur_ypos

#Some test code
black = Ball('solid', 'black', 8, 0, 0)
black.collideBall(60, np.pi/4, 0, 0)
print black.currentVel(time.time())
print black.currentPos(time.time())
time.sleep(2)
print black.currentVel(time.time())
print black.currentPos(time.time())
time.sleep(2)
print black.currentVel(time.time())
print black.currentPos(time.time())
time.sleep(2)
print black.currentVel(time.time())
print black.currentPos(time.time())
time.sleep(2)
print black.currentVel(time.time())
print black.currentPos(time.time())