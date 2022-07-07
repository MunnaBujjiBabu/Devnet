from this import s


class Router:
    def __init__(self, model, swversion, ip_address):
        self.model = model
        self.swversion = swversion
        self.ip_address = ip_address
    def getdesc(self):
        desc = (f'Router Model:         :{self.model}\n'
                f'swversion:  :         :{self.swversion}\n'
                f'ip_address: :         : {self.ip_address}\n ')
        return desc

class switch(Router):
    def getdesc(self):
        desc = (f'Switch Model:         :{self.model}\n'
                f'swversion:  :         :{self.swversion}\n'
                f'ip_address: :         : {self.ip_address}\n ')
        return desc

rtr1=Router('c100v', '14.2', '11.11.0.2')
sw1=Router('switch', '10.1', '8.8.8.8')
print(sw1.getdesc())