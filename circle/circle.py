from math import pi

class Circle:
	def __init__(self, r=1):
		if r >= 0:
			self._radius = r
		else:
			raise ValueError("radius cannot be negative")

	@property
	def radius(self):
		return self._radius

	@radius.setter		
	def radius(self, val):
		if val < 0:
			raise ValueError("radius cannot be negative")
		else:
			self._radius = val
			return self._radius

	@property  # lets a method be accessed as an attribute instead of a method
	def diameter(self):
		return self.radius * 2

	@diameter.setter  # allows you to work backwards
	def diameter(self, val):
		if val >= 0:
			self.radius = val / 2
		else:
			raise ValueError("Diameter cannot be negative.")
		
	@property
	def area(self):
		return pi * self.radius ** 2
	
	@area.setter
	def area(self, val):
		raise AttributeError("Can't set the area.")

	def __repr__(self):
		return f'Circle({self.radius})'

if __name__ == '__main__':
	c = Circle()
	print(c)
	c.radius = -15
	print(c)