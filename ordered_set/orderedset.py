
class OrderedSet:
	def __init__(self, args):
		self.args = []
		for arg in args:
			if arg not in self.args:
				self.args.append(arg)

	def __iter__(self):
		for val in sorted(self.args):
			yield val

	def __contains__(self, key):  # allows for the use of in on the object
		return key in self.args
