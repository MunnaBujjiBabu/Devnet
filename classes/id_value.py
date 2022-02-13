import ctypes
value = 20
memory_location = id(value)
print ("memory location:", memory_location)
print (ctypes.cast(memory_location, ctypes.py_object).value)
