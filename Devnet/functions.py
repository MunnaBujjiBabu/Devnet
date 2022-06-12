def sub(arg1,arg2):
    result = arg1-arg2
    return result
print (sub(10,5))

def hello(*args):
    for arg in args:
        print("hello", arg)
hello("asdfasd", "asdf" , "qwerqwe")

def hello(**kwargs):
    for key, value in kwargs.items():
        print("hello", key, " ", value)
hello(t1="aaaa", t2="bbbb")