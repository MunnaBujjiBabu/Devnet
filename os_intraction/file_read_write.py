#file = open("disk_process_usage.py")
#print(file.readline())
#print(file.read())
#print(type(file))
#file.close()

#with open("disk_process_usage.py") as file:
#	print(file.read())

"""
with open("disk_process_usage.py") as file:
	for line in file:
		print(line.upper().strip())


with open("disk_process_usage.py") as file:
	lines = file.readlines()
	lines.sort()
	print(lines)
"""

with open("novel.txt", 'w') as file:
	file.write("test test test test test")
	
with open("novel.txt", 'a') as file1:
	file1.write("qa qa qa qa")

