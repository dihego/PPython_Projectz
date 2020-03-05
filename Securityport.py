#!/usr/bin/env python
import os
import re
import time
from datetime import datetime
import sys
from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
from Exscript import Host, Account
i = datetime.now()
e = i.strftime('%H:%M:%S %Y/%m/%d')
d = i.strftime('%Y_%m_%d')
os.system('clear')
print "############\n","###############\n","############\n"


print "*******************************************************************"
print "* Quick enable PortSecurity  -                           *"
print "*  NWFCU - Authorized users only                            *"
print "*                         	   				  *"
print "* "	+ e + 		                     "  						  *"
print "*******************************************************************" 
print "PortSecurity"
print
print
print '''
Refer to the emails generated for the below information.
Failure to do may cause routing issues within the environment

'''

print "*******************************************************************" 
print "*******************************************************************" 
accountcore = read_login()
print



userhostname = raw_input("Enter Hostname: ")
usermac = raw_input("Enter MAC address: ")
userinterface = raw_input("Enter Interface: ")
time.sleep(4)
os.system('clear')
print
print "*******************************************************************" 
print "*******************************************************************" 





def portsecurityaddresschecker(hostname,violationMAC):
	try:
		#print hostname
		conn = SSH2(verify_fingerprint = False)
		conn.connect(hostname)
		conn.login(accountcore)

		conn.execute('terminal length 0')
		#verifyotherports = 'show port-security address'
		verifyotherports = 'show port-security address | inc ' + violationMAC
		conn.execute(verifyotherports)
		stringtomatch = conn.response
		stringtomatch2 = str(stringtomatch)
		#print stringtomatch2
		#time.sleep(5)
		print "*******************************************************************" 
		print "*******************************************************************" 


		if 'SecureSticky' in stringtomatch2:
			print "MAC is already configured under a different interface "

			print
			print
			print "Flushing that out first "
			for item in stringtomatch.split("\n"):
				if violationMAC in item:
					splitting = item.split()
					#print item
		               	print item.strip()

			print "************"
			print "************"
			print "************"


			cmd1 = "sho run int " + splitting[3]
			#print cmd1
			conn.execute(cmd1)
			print conn.response
			time.sleep(4)
			conn.execute("configure terminal")
			#print conn.response
			#print "configure terminal"
			cmd2 = "interface " + splitting[3]
			#print cmd2
			conn.execute(cmd2)
			#print conn.response
			conn.execute("shut")
			#print conn.response
			#print "shut"
			time.sleep(3)
			conn.execute("no switchport port-security")
			#print conn.response
			#print "no switchport security"
			time.sleep(3)
			conn.execute("no switchport port-security mac-address sticky ")
			#print conn.response
			#print "no switcheport security mac sticky"
			cmd3 = "do clear arp interface " + splitting[3]
			time.sleep(3)
			#print cmd3
			conn.execute(cmd3)
			#print conn.response
			conn.execute("switchport port-security mac-address sticky ")
			#print conn.response
			#print "switchport portsecurity mac sticky"
			#conn.execute("switchport portsecurity mac sticky")
			#print conn.response
			conn.execute("switchport port-security")
			#print conn.response
			#print "switchport portsecurity"
			conn.execute("no shut")

			#print conn.response
			time.sleep(3)
			#print "no shut"
			conn.execute("end")
			#print "end"
			#print conn.response



		else:
			
			print "Nothing here"

	except:
		print "Something went wrong... Please try again!!!!!!!!!!!!!"


def originalviolator(hostname,intefaceaffected):
	#os.system('clear')
	print "*******************************************************************" 
	print "*******************************************************************" 
	print "NOW clearing out the interface that was violated"
	print
	print
	print "Take note of the current configuration:  "
	print "VLAN for VOICE/DATA"
	print "MAX MACs allowed!!!"
	print
	print "************"
	print "************"
	conn = SSH2(verify_fingerprint = False)
	conn.connect(hostname)
	conn.login(accountcore)
	conn.execute('terminal length 0')
	cmd1 = "sho run int " + intefaceaffected
	conn.execute(cmd1)
	print conn.response
	time.sleep(3)
	print
	print
	print
	max_2macs = raw_input("Is the PC hookedup through the phone? : (Y/N) ")
	#if max_2macs.upper([0]) == 'Y'
	if max_2macs in ['Yes','YES','y','Y','ye','Ye','yes']:
		conn.execute("configure terminal")
		#print conn.response
		cmd2 = "interface " + intefaceaffected
		conn.execute(cmd2)
		#print conn.response
		conn.execute("shut")
		#print conn.response
		conn.execute("no switchport port-security")
		#print conn.response
		conn.execute("no switchport port-security mac-address sticky")
		#print conn.response
		cmd3 = "do clear arp interface " + intefaceaffected
		conn.execute(cmd3)
		#print conn.response
		conn.execute("switchport port-security max 2")
		conn.execute("switchport port-security mac-address sticky")
		#print conn.response
		conn.execute("switchport port-security")
		#print conn.response
		conn.execute("no shut")
		#print conn.response
		conn.execute("end")
		#print conn.response
		print
		print
                cmd4 = "show run interface " + intefaceaffected
		conn.execute(cmd4)
		print conn.response
	else:

		conn.execute("configure terminal")
		#print conn.response
		cmd2 = "interface " + intefaceaffected
		conn.execute(cmd2)
		#print conn.response
		conn.execute("shut")
		#print conn.response
		conn.execute("no switchport port-security")
		#print conn.response
		conn.execute("no switchport port-security mac-address sticky")
		#print conn.response
		cmd3 = "do clear arp interface " + intefaceaffected
		conn.execute(cmd3)
		#print conn.response
		conn.execute("switchport port-security mac-address sticky")
		#print conn.response
		conn.execute("switchport port-security")
		#print conn.response
		conn.execute("no shut")
		#print conn.response
		conn.execute("end")
		print
		print
                cmd4 = "show run interface " + intefaceaffected

		conn.execute(cmd4)
		print conn.response	

	
def main(hostname,violationMAC,intefaceaffected):
	print "Verifying if mac address is already associated with another interface within the same switch..."
	print
	portsecurityaddresschecker(hostname,violationMAC)
	print "Please wait..."
	time.sleep(5)

	originalviolator(hostname,intefaceaffected)

	






exit = True
while exit:
	if re.search(r'(^h2\w+|^h1\w+|^s\w+)',userhostname):
		print ""
		main(userhostname,usermac,userinterface)
		break

	else:
		print '''The device you are trying to execute is not a switch and not Authorized!!!!!!!!'''
		print
		print "Please entered a valid hostname"
		userhostname = raw_input("Enter Hostname: ")
		print
		print

#		while True:


#h24swh h24swde h24swg h24swab h23swabc h2swlogs h22swab h22swmort h24swi h24swf h24swr2 h25swa h212da h212va h211va






#print stringtomatch



