class Apple:
	"""apple color & flavour"""
	def __init__(self, color, flavour):
		self.color = color
		self.flavour = flavour
	def __str__(self):
		return "this apple is {} and {}".format(self.color, self.flavour)
instance3 = Apple("red", "sweet")
print(instance3.color)
print(instance3)
