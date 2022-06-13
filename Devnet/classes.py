from pydoc import describe


class Router:
    '''router class'''
    def __init__ (self, model, swversion, ip_address):
        self.model = model
        self.swversion = swversion
        self.ip_address = ip_address
rtr1=Router('c100v', '14.2', '11.11.0.2')
print(rtr1.model)
rtr2=Router('C200v', '14.0', '8.8.8.8')
print(rtr2.model)


class Router:
    def __init__(self, model, swversion, ip_address):
        self.model = model
        self.swversion = swversion
        self.ip_address = ip_address
    def getdesc(self):
        desc = f'Router model      :{self.model}\n'\
               f'swversion         :{self.swversion}\n'\
               f'ip_address        :{self.ip_address}'
        return desc
    def test(self):
        print('test')
rtr1=Router('c100v', '14.2', '11.11.0.2')
rtr2=Router('C200v', '14.0', '8.8.8.8')
print(rtr1.test())
print(rtr1.getdesc(), sep='')