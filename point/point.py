class Point():
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z
		# self = (x,y,z) ... can be unpacked with multiple assignment
	def __repr__(self):
		return f'Point(x={self.x}, y={self.y}, z={self.z})'

	def __eq__(self, other):  # operating overloading
		return (self.x, self.y, self.z) == (other.x, other.y, other.z)  # compared deeply

	def __add__(self, other):  # operating overloading
		return Point(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, val):
		return Point(self.x * val, self.y * val, self.z * val)

	def __rmul__(self, val):
		return self.__mul__(val)

	def __iter__(self):  # creates an iterable when called, not an iterator
		# multiple assignment loops over objects the same way "for" loops do
		yield self.x
		yield self.y
		yield self.z
		# or: return iter((self.x, self.y, self.z))
		# or: yield from (self.x, self.y, self.z)
			# the yield from statement loops over the new tuple we created and yields the values