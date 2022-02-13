import re
test = re.split(r"([,.?!])", "HI, this is one sentense. This the second.")
print (test)

print(re.sub(r"^([\w]*)+([\w]*)$", r"\2 \1", "Munna Bujji"))

data = input("this comes from STDIN:")
print("this writes to STDOUT:")
print("this generated from STDERR" + data+ 1)
