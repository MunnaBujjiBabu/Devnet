import csv
sample_file = open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/csvdata.csv')
sample_reader = csv.reader(sample_file)
sample_data = list(sample_reader)
print(sample_data[1])

with open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/csvdata.csv') as data:
    csv_list = list(csv.reader(data))
    for i in csv_list:
        device = i[0]
        ip_address = i[1]
        location = i[2]
        print("device: ", device, "ip_address: ", ip_address, "location: ", location)
    

    def fibbonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    def ssh(ip_address):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, username='root', password='cisco')
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('show version')
        print(ssh_stdout.read())
        ssh.close()

    def ip_address(ip_address):
        import socket
        try:
            socket.inet_aton(ip_address)
            return True
        except socket.error:
            return False

import re
def valid_ip(ip):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)

def valid_mac(mac):
    return re.match(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$", mac)

import json
def valid_json(json_data):
    try:
        json.loads(json_data)
        return True
    except ValueError:
        return False
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n-1)

def telnet(ip_address):
    import telnetlib
    tn = telnetlib.Telnet(ip_address)
    tn.read_until(b"Username: ")
    tn.write(b"root\n")
    tn.read_until(b"Password: ")
    tn.write(b"cisco\n")
    tn.write(b"show version\n")
    print(tn.read_all().decode('ascii'))

def ssh(ip_address):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username='root', password='cisco')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('show version')
    print(ssh_stdout.read())
    ssh.close()

def fibbanocci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbanocci(n-1) + fibbanocci(n-2)

def multiplication(n):
    if n == 0:
        return 1
    else:
        return n * multiplication(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def ssh(ip_address):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username='root', password='cisco')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('show version')
    print(ssh_stdout.read())
    ssh.close()


def fibbanocci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbanocci(n-1) + fibbanocci(n-2)

def telnet(ip_address):
    import telnetlib
    tn = telnetlib.Telnet(ip_address)
    tn.read_until(b"Username: ")
    tn.write(b"root\n")
    tn.read_until(b"Password: ")
    tn.write(b"cisco\n")
    tn.write(b"show version\n")
    print(tn.read_all().decode('ascii'))

def ssh(ip_address):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_address, username='root', password='cisco')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('show version')
    print(ssh_stdout.read())
    ssh.close()

def valid_ip(ip):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)

def valid_mac(mac):
    return re.match(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$", mac)

def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and palindrome(word[1:-1])