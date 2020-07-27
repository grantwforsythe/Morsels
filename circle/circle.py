from math import pi

class Circle:
	def __init__(self, r=1):
		self.radius = r


	@property
	def radius(self):
		return self._radius


	@radius.setter		
	def radius(self, val):
		if val < 0:
			raise ValueError("radius cannot be negative")
		self._radius = val
			

	# we don't need to check if the diameter is negative because it calls the radius property setter	
	@property  # lets a method be accessed as an attribute instead of a method
	def diameter(self):
		return self.radius * 2


	@diameter.setter  # allows you to work backwards
	def diameter(self, val):
		self.radius = val / 2
		

	@property
	def area(self):
		return pi * self.radius ** 2
	
	# we don't need this. by trying to set the property, it will raise an error
	# @area.setter
	# def area(self, val):
	# 	raise AttributeError("Can't set the area.")

	def __repr__(self):
		return f'Circle({self.radius})'


if __name__ == '__main__':
	c = Circle()
	print(c)
	c.radius = -15
	print(c)