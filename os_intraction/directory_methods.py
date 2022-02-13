import os
dir = "junk"
for name in os.listdir(dir):
	fullname = os.path.join(dir, name)
	if os.path.isdir(fullname):
		print("{} is directory".format(fullname))
	else:
		print("{} is file:".format(fullname))
