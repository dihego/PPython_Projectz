#!/bin/python
import os
import paramiko,sys
import getpass
os.system('clear')
passwordz =getpass.getpass("Password: ")

hostnamee = 'hostnamehere'
usernamee = 'username'
passw = '$'
port = 22
mypath='/export/home/usertest/boxes'
remotepath='/export/home/usertest/'


t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=passwordz)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('boxes',mypath)

ssh.close()
