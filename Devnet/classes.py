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