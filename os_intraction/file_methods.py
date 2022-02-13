import os
import datetime

if os.path.exists("novel.txt") == True: 
	os.remove("novel.txt")

print(os.path.exists("novel.txt"))

print(os.path.getsize("areas.py"))

t1 = os.path.getmtime("areas.py")
print(datetime.datetime.fromtimestamp(t1))

print(os.path.abspath("areas.py"))


print(os.listdir("junk"))
