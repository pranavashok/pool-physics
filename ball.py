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

	def collideBall(power, angle, xoffset, yoffset):
		time = time() #Time at hit
		xvel += power*cos(angle)
		yvel += power*sin(angle)

	def currentVel():
		cur_time = time()
		cur_xvel = xvel - FRICTION*G*(cur_time-time)
		cur_yvel = yvel - FRICTION*G*(cur_time-time)
		return cur_xvel, cur_yvel
	
	def currentPos():
		cur_time = time()
		cur_xpos = xvel*(cur_time-time) - 0.5*FRICTION*G*(cur_time-time)*(cur_time-time)
		cur_ypos = yvel*(cur_time-time) - 0.5*FRICTION*G*(cur_time-time)*(cur_time-time)
		return cur_xpos, cur_ypos