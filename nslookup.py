#!/usr/bin/env python                                                                                                                                    
import os                                                                                                                                                
import sys                                                                                                                                               
os.system('clear')                                                                                                                                       
print "Copy and Paste name of hosts you would like to query: "                                                                                           
print "CTR^D to quit and query hosts ********** "                                                                                                        
lista = list()                                                                                                                                           
userinput = sys.stdin.read().split()                                                                                                                     
lista.append(userinput)                                                                                                                                  
print                                                                                                                                                    
print "*********"                                                                                                                                        
print "Commands - ex: nslookup,host, dig, traceroute :  "                                                                                                
cmd = raw_input("")                                                                                                                                      
print "*********"                                                                                                                                        
for z in lista:                                                                                                                                          
        print "Number of Hosts: ",len(z)                                                                                                                 
        for q in z:                                                                                                                                      
                cmd1 =  cmd + " " + q                                                                                                                    
                print q, os.system(cmd1)                                                                                                                 
                print "************************"                                                                                                         
                print "Next******"                                                                                                                       
                                                                                                                                                         
print "************************"                                                                                                                         
print                                                                                                                                                    
print "Done!"
 
