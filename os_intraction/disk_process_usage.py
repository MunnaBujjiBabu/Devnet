import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	print (du)
	print(type(du))
	free = du.free/du.total * 100
	check_disk_usage.free1 = du.free/du.total * 100
	#print(free)
	return free 
	
def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage
	
print(check_disk_usage("/"))
print(check_cpu_usage())
"""
if not check_disk_usage("/"):
	print ("Error")
	print (check_disk_usage.free)
else: 
	print(check_disk_usage.free)
"""
