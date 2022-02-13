class Piglet:
	name = "piglet"
	age = 0
	def voice(self):
		print("oink i am {} oink".format(self.name))
	def pigage(self):
		print("age is {} ".format(self.age*18))
	
instance1 = Piglet()
instance1.voice()

instance2 = Piglet()
instance2.name = "piglet2"
instance2.voice()
instance2.age = 2
instance2.pigage()
