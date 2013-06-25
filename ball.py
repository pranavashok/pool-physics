import numpy as np

class Ball:
	xvel = 0.0
	yvel = 0.0
	time = 0.0
	
	def __init__(type, color, number, xpos, ypos):
		self.type = type
		self.color = color
		self.number = number
		self.xpos = xpos
		self.ypos = ypos
		self.inmotion = 0

	def collideBall(vel, angle, xoffset, yoffset):
		self.inmotion = 1
		self.time = time() #Time at hit
		self.xvel += vel*np.cos(angle)
		self.yvel += vel*np.sin(angle)

	def currentVel():
		cur_time = time()
		elapsed_time = self.time - cur_time
		cur_xvel = self.xvel - FRICTION*G*elapsed_time
		cur_yvel = self.yvel - FRICTION*G*elapsed_time
		return cur_xvel, cur_yvel
	
	def currentPos():
		cur_time = time()
		elapsed_time = self.time - cur_time
		cur_xpos = self.xvel*elapsed_time - 0.5*FRICTION*G*np.square(elapsed_time)
		cur_ypos = self.yvel*elapsed_time - 0.5*FRICTION*G*np.square(elapsed_time)
		return cur_xpos, cur_ypos