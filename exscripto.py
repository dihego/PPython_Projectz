#!/usr/local/bin/python2.7 
import sys
#sys.path.append('/usr/lib/python2.6/site-packages/exscript-master')
from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
from Exscript import Host, Account
import os
import re
import time
from datetime import datetime
import getpass
import paramiko, sys

#os.system('rm logfile')
#os.system('rm output')

#logfiles = 'logfile'
#logfiless = 'output'

i = datetime.now()
e = i.strftime('%H:%M:%S %Y/%m/%d')
d = i.strftime('%Y_%m_%d')
os.system('clear')

print "*******************************************************************"
print "* Making Queries & Changes per device -                           *"
print "*  Schwab - Authorized users only                            *"
print "*                         	   				  *"
print "* "	+ e + 		                     "  						  *"
print "*******************************************************************" 
print
print
print "Regular"
accountcore = read_login()
print 
#print "Verizon Password "
#accountbranch = read_login()

#print "Aruba"
#print "Username alraedy entered"
#Passwordz = getpass.getpass("Password: ")


#paramiko.util.log_to_file("/NAS_ddos_tools/VNSS_Nocc/.logs/allVerbose")
ssh3 = paramiko.SSHClient()

class devicesF:
	##filename=open('logfiless','a')

	
	def Branch(self,host_ips,cmdz,timez):
		print "ASA"
		#archivo_por_nombre = "/NAS_ddos_tools/VNSS_Nocc/.logs/" + username_vrz + "_logBR_" + d
		#filename=open(archivo_por_nombre,'a')
		try:
			print host_ips
			conn = SSH2(verify_fingerprint = False)
			conn.connect(host_ips)
			conn.login(accountbranch)
			print
			for h in cmdz:
				listastring = str(h)
				conn.execute(listastring)
				print conn.response
				print
				print
				print
				#filename.write('\n')
				#filename.write("*************** \n")
				#filename.write(timez)
				#filename.write('\n')			
				#filename.write(host_ips)
				#filename.write('\n')
				#filename.write('\n')
				#filename.write(view_print)
				#filename.write("*************** \n")
				#filename.write("*************** \n")

			time.sleep(2)
			#filename.close()
			print
			print "********************************"
			print "Hosts CHECKED!    ++BRANCH+++"
			print "********************************"
		except:
			print "IP for this device : ", host_ips
			print "Incorrect commands or host not available...."



	def Core(self,host_ips,cmdz,timez):
		print "Core"
		#archivo_por_nombre = "/NAS_ddos_tools/VNSS_Nocc/.logs/" + usernamee + "_logC_" + d
		#filename=open(archivo_por_nombre,'a')
		try:
			print host_ips
			conn = SSH2(verify_fingerprint = False)
			conn.connect(host_ips)
			conn.login(accountcore)
			print
			for h in cmdz:
				listastring = str(h)
				conn.execute(listastring)
				print conn.response
				print 
				print 
				print
				#filename.write('\n')
				#filename.write("*************** \n")
				#filename.write(timez)
				#filename.write('\n')			
				#filename.write(host_ips)
				#filename.write('\n')
				#filename.write('\n')
				#filename.write(view_print)
				#filename.write("*************** \n")
				#filename.write("*************** \n")




			time.sleep(2)
			#filename.close()
			print
			print "********************************"
			print "Hosts CHECKED!   +++REGULAR++++"
			print "********************************"
		except:
			print
			print "IP for this device : ", host_ips
			print "Incorrect commands or host not available...."




c_schwab = devicesF()


devices = ['* Juniper/CISCO/F5/Linux Boxes ','REGULAR___QUIT']
exit = True
while exit:

	print "Copy and Paste name of hosts you would like to query: "                                                                                           
	print "CTR^D to quit and query hosts ********** "                                                                                                        
	listaJ = list()
	listafinal = list()
	listaJN = len(listafinal)
	hostsinput = sys.stdin.read().split()                                                                                                                     
	listaJ.append(hostsinput)


	print
	print
	for z in listaJ:
		print "*********************************"
		for q in z:
			listafinal.append(q)
		#stringg = str(z)
		#listafinal.append(stringg)
	if re.search(r'(dc7ravpnfw|RBRA0\w+[a-z]|[A-Z]\.\w+[a-z]|[A-Z]|xbra0\w+[a-z]|[A-Z]\.\w+[a-z]|[A-Z]|XBRA0\w+[a-z]|[A-Z]\.\w+[a-z]|[A-Z])',str(listafinal)):
		lista_commands = list()
		while True:
			maxlines1 = raw_input("Number of commands YOU WOULD LIKE TO QUERY : ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',maxlines1):
				print "Is not a number!"
			elif len(maxlines1.strip()) == 0 :
				print "No input"
			elif maxlines1 in ['exit',"^D",',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try Again"
			else:
				break
		maxlines2 = int(maxlines1)
		for lines in range(maxlines2):
			inline = raw_input("")
			lista_commands.append(inline)
		print "*****************"
		print "*****************"
		cc=0
		while cc < len(listafinal):
			stringhosts = str(listafinal[cc])
			c_schwab.Branch(stringhosts,lista_commands,e)
			cc+=1
			print
		for zika in  listafinal:
			print zika
		print

		for repeticion in lista_commands:
			print repeticion
		print
		#print "*****************"
		print "***************** CTRL ^C to Quit!!! *****************"
		print "set cli screen-length 0"
		print "terminal length 0"
		print "******************************************************"

	else:

		lista_commands = list()
		while True:
			maxlines1 = raw_input("Number of commands YOU WOULD LIKE TO QUERY : ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',maxlines1):
				print "Is not a number!"
			elif len(maxlines1.strip()) == 0 :
				print "No input"
			elif maxlines1 in ['exit',"^D",',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try Again"
			else:
				break

		maxlines2 = int(maxlines1)
		for lines in range(maxlines2):
			inline = raw_input("")
			lista_commands.append(inline)
		print "*****************"
		print "*****************"
		cc=0
		while cc < len(listafinal):
			stringhosts = str(listafinal[cc])
			c_schwab.Core(stringhosts,lista_commands,e)
			cc+=1
			print
		for zika in  listafinal:
			print zika
		print

		for repeticion in lista_commands:
			print repeticion
		print
				#print "*****************"
		print "***************** CTRL ^C to Quit!!! *****************"
		print "set cli screen-length 0"
		print "terminal length 0"
		print "******************************************************"


