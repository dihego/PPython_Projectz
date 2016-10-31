#!/bin/python
import os,sys
import time
import random
from random import randint 
os.system('clear')

palabras_lista = ['minute','refer','busy','ought','absence','amusement','ache','aches','folk','celebration','folks',
'business','busy','recent','nation','various','vary','absent','conference','decision','decide','confer','entitle','wednesday','political','really','national','real']

#lista_Cisco_ = list()
#maxlines2 = int(input("Number of WORDS : "))
#for lines in range(maxlines2):
#	inline = raw_input("Words : ")
#	lista_Cisco_.append(inline)

os.system('clear')
def sebastian(listawrd,mactalk):
	trialz=0
	print "Spell the word..."
	os.system('say ' + listawrd)
	answer = ''
	while answer != listawrd:
		spellingw = raw_input(": ")
		if spellingw == listawrd:
			print "good"
			break
		elif trialz == 5:
			print
			print
			print "THE Word is: "
			print listawrd
			break
		else:
			os.system('say ' + listawrd)
			print "Try again"
			trialz+=1
	print
	print "***************************"



speech = ""
i=0
while i < len(palabras_lista):
	list_to_str = str(palabras_lista[i])
	#virginian = "virginian"
	speech = 'say '
	sebastian(list_to_str,speech)
	i+=1

print "You are Done!"
