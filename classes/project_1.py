import ctypes

class Event:
	def __init__(self, event_date, event_type, machine_name, user):
		self.date = event_date
		self.type = event_type
		self.machine = machine_name
		self.user = user
		
events = [
	Event('2020-01-21 12:23:34', 'login', 'workstation1.local', 'jordan1'),
	Event('2020-03-21 12:23:34', 'login', 'workstation2.local', 'jordan2'),
	Event('2020-02-21 12:23:34', 'login', 'workstation5.local', 'jordan5'),
	Event('2020-05-21 12:23:34', 'login', 'workstation3.local', 'jordan3'),
	Event('2020-10-21 12:23:34', 'logout', 'workstation1.local', 'jordan1'),
	Event('2020-04-21 12:23:34', 'login', 'workstation2.local', 'jordan6'),
	Event('2020-06-21 12:23:34', 'login', 'workstation.4local', 'jordan4'),
	]

def get_event_date(event):
	print (event.date)
	return event.date
	
def current_users(events):
	events.sort(key=get_event_date)
	#events.sort1 = events.sort(key=get_event_date)
	print("\n")
	print (events)
	print("\n")
	machines = {}
	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set ()
		if event.type == "login":
			machines[event.machine].add(event.user)
		elif event.type == "logout":
			machines[event.machine].remove(event.user)
	return machines
	
def generate_report(machines):
	for machines, users in machines.items():
		if len(users) > 0:
			user_list = ", ".join(users)
			print("{}: {}".format(machine, user_list))

users = current_users(events)
print(users)
