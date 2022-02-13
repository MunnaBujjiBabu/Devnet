class Animal:
	sound = ""
	def __init__(self, name):
		self.name = name
	def voice(self):
		print("{sound} i am {name} {sound}".format(name=self.name, sound= self.sound))
		
class Piglet(Animal):
	sound = "oink"
	
class Cow(Animal):
	sound = "moooo"

instance1 = Piglet("pig")
instance1.voice()

instance2 = Cow("Cowwy")
instance2.voice()
