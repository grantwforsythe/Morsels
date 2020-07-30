from math import pi

class Circle():
	def __init__(self, radius = 1):
		if radius < 0:
			raise ValueError
		else:
			self.radius = radius

	@property
	def radius(self):
		return self._radius
	
	@radius.setter
	def radius(self, val):
		self._radius = val

	@property
	def diameter(self):
		return self._diameter

	@diameter.setter
	def diameter(self, val):
		if val < 0:
			raise ValueError
		else:
			self.radius = val /2
			self._diameter = val
	
	@property
	def area(self):
		return pi * self.radius ** 2

	def __repr__(self):
		return f'Circle({self.radius})'


if __name__ == '__main__':
	c = Circle()
	c.radius = -1
	print(c.radius)
	c.diameter = 10
	print(c.radius)