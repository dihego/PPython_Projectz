gifrom random import randint
import os
import re
import time
from datetime import datetime

os.system('clear')

##This is to ensure user enters INT and not STR
while True:
	userinput_maxoperations = raw_input("How many operations : ")
	if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_maxoperations):
		print "Is not a number!"
	elif len(userinput_maxoperations.strip()) == 0 :
		print "No input"
	elif userinput_maxoperations in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
		print "Try again"
	else:
		break


def multiplicationz(userinput_maxoperations):
	quit = "0"
	lista = list()
	wrong_str = list()
	wrong_int = list()
	two_wrong_str_list = list()
	two_wrong_int_list = list()
	two_lista = list()


	#For loop to do math - 
	for line in range(int(userinput_maxoperations)):
		a = randint(1,9)
		b = randint(2,9)
		operation = a * b
		operation2 = str(a) + " * " + str(b) + ":"
		print operation2
		while True: 
			userinput_answer = raw_input("Answer: ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_answer):
				print "Is not a number!"
			elif len(userinput_answer.strip()) == 0 :
				print "No input"
			elif userinput_answer in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try again"

			else:
				break
		userinput_answerToint = int(userinput_answer)
		if userinput_answerToint != operation:
			print "oops"
			print
			print
			wrong_int.append(operation)
			wrong_str.append(operation2)

	total_entered = len(lista)
	total_wrong = len(wrong_str)
	#total = int(total_entered)- int(total_wrong)
	userinput_maxoperations_int = int(userinput_maxoperations)
	wrong_str_lenght = len(wrong_str)
	total = userinput_maxoperations_int - wrong_str_lenght
	print "Calculating..."
	time.sleep(3)
	print "=================================================================="
	print "You got ", total , " out of ", userinput_maxoperations, " CORRECT!"
	print "------------------"
	print "Summary.... "
	time.sleep(2)
	print "Incorrect operations!"
	for lista_incorrecta in wrong_str:
		print lista_incorrecta
	print "Only : ",len(wrong_str)
	if len(wrong_str) == 0:
		print "Congrats... You are done"
		time.sleep(2)
		os.system('clear')
	else:
		print	
		print
		print
		print "------------------------"
		time.sleep(5)
		os.system('clear')
		print "Let's try again with the ones you got incorrect: "
		##Function to to redo the incorrect ones
		def tryingagain():
			while True: 
				userinput_tryagain = raw_input("Answer: ")
				if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain):
					print "Is not a number!"
				elif len(userinput_tryagain.strip()) == 0 :
					print "No input"
				elif userinput_tryagain in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
					print "Try again"
				else:
					break
			userinput_tryagain_int = int(userinput_tryagain)
			if userinput_tryagain_int != int(wrong_int_index):
				print "oops"
				print
				print
				two_wrong_str_list.append(wrong_str_index)
				two_wrong_int_list.append(wrong_int_index)
		i=0
		c=0 
		while i< total_wrong:
			wrong_str_index = str(wrong_str[i])
			wrong_int_index = str(wrong_int[c])
			print str(wrong_str[i])
			tryingagain()
			i+=1
			c+=1
		if len(two_wrong_str_list) == 0 :
			print "Congrats.... You are done"
			time.sleep(2)
			os.system('clear')
		else:

			print "Calculating...."
			time.sleep(5)
			os.system('clear')
			print "===================================="
			print "Incorrect operations:"
			print "-------"
			iii=0
			ccc=0
			for juniper in two_wrong_str_list:
				wrong_str_index = (two_wrong_str_list[iii])
				wrong_int_index = (two_wrong_int_list[ccc])
				print wrong_str_index
				iii+=1
				ccc+=1
			print
			print
			print
			print "You are almost done - Lets review the ones you still got incorrect!"
			ii=0
			cc=0
			total_wrong2 = len(two_wrong_str_list)

			while ii< total_wrong2:
				wrong_str_index2 = str(two_wrong_str_list[ii])
				wrong_int_index2 = str(two_wrong_int_list[cc])
				print wrong_str_index2
				invalid = True
				while invalid:
					userinput_tryagain1 = raw_input("Answer: ")
					if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain1):
						print "Is not a number!"
					elif len(userinput_tryagain1.strip()) == 0 :
						print "No input"
					elif userinput_tryagain1 == wrong_int_index2:
						print ("Good!")
						invalid = False
					else: 
						print ("try again")
						print
						print
						
				ii+=1
				cc+=1
			print ("You are now done!")
			os.system('clear')


def subtractingz(userinput_maxoperations):
	os.system('clear')
	quit = "0"
	lista = list()
	wrong_str = list()
	wrong_int = list()
	two_wrong_str_list = list()
	two_wrong_int_list = list()
	two_lista = list()

	#For loop to do math - 
	for line in range(int(userinput_maxoperations)):
		a = randint(20, 99)
		b = randint(1, 20)
		operation = a - b
		operation2 = str(a) + " - " + str(b) + ":"
		print operation2
		while True: 
			userinput_answer = raw_input("Answer: ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_answer):
				print "Is not a number!"
			elif len(userinput_answer.strip()) == 0 :
				print "No input"
			elif userinput_answer in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try again"
			else:
				break
		userinput_answerToint = int(userinput_answer)
		if userinput_answerToint != operation:
			print "oops"
			print
			print
			wrong_int.append(operation)
			wrong_str.append(operation2)

	total_entered = len(lista)
	total_wrong = len(wrong_str)
	#total = int(total_entered)- int(total_wrong)
	userinput_maxoperations_int = int(userinput_maxoperations)
	wrong_str_lenght = len(wrong_str)
	total = userinput_maxoperations_int - wrong_str_lenght
	print "Calculating..."
	time.sleep(3)
	print "=================================================================="
	print "You got ", total , " out of ", userinput_maxoperations, " CORRECT!"
	print "------------------"
	print "Summary.... "
	time.sleep(2)
	print "Incorrect operations!"
	for lista_incorrecta in wrong_str:
		print lista_incorrecta
	print "Only : ",len(wrong_str)
	if len(wrong_str) == 0 :
		print "Congrats... You are done"
		time.sleep(2)
		os.system('clear')
	else:
		print	
		print
		print
		print "------------------------"
		time.sleep(5)
		os.system('clear')
		print "Let's try again with the ones you got incorrect: "
		##Function to to redo the incorrect ones
		def tryingagain():
			while True: 
				userinput_tryagain = raw_input("Answer: ")
				if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain):
					print "Is not a number!"
				elif len(userinput_tryagain.strip()) == 0 :
					print "No input"
				elif userinput_tryagain in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
					print "Try again"
				else:
					break
			userinput_tryagain_int = int(userinput_tryagain)
			if userinput_tryagain_int != int(wrong_int_index):
				print "oops"
				print
				print
				two_wrong_str_list.append(wrong_str_index)
				two_wrong_int_list.append(wrong_int_index)
		i=0
		c=0 
		while i< total_wrong:
			wrong_str_index = str(wrong_str[i])
			wrong_int_index = str(wrong_int[c])
			print str(wrong_str[i])
			tryingagain()
			i+=1
			c+=1
		if len(two_wrong_str_list) == 0 :
			print "Congrats.... You are done"
			time.sleep(2)
			os.system('clear')
		else:
			print "Calculating...."
			time.sleep(5)
			os.system('clear')
			print "===================================="
			print "Incorrect operations:"
			print "-------"
			iii=0
			ccc=0
			for juniper in two_wrong_str_list:
				wrong_str_index = (two_wrong_str_list[iii])
				wrong_int_index = (two_wrong_int_list[ccc])
				print wrong_str_index
				iii+=1
				ccc+=1
			print
			print
			print
			print "You are almost done - Lets review the ones you still got incorrect!"
			ii=0
			cc=0
			total_wrong2 = len(two_wrong_str_list)

			while ii< total_wrong2:
				wrong_str_index2 = str(two_wrong_str_list[ii])
				wrong_int_index2 = str(two_wrong_int_list[cc])
				print wrong_str_index2
				invalid = True
				while invalid:
					userinput_tryagain1 = raw_input("Answer: ")
					if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain1):
						print "Is not a number!"
					elif len(userinput_tryagain1.strip()) == 0 :
						print "No input"
					elif userinput_tryagain1 == wrong_int_index2:
						print ("Good!")
						invalid = False
					else: 
						print ("try again")
						print
						print
						
				ii+=1
				cc+=1
			print ("You are now done!")
			os.system('clear')


def addingz(userinput_maxoperations):
	os.system('clear')
	quit = "0"
	lista = list()
	wrong_str = list()
	wrong_int = list()
	two_wrong_str_list = list()
	two_wrong_int_list = list()
	two_lista = list()


	#For loop to do math - 
	for line in range(int(userinput_maxoperations)):
		a = randint(1, 99)
		b = randint(1, 99)
		operation = a + b
		operation2 = str(a) + " + " + str(b) + ":"
		print operation2
		while True: 
			userinput_answer = raw_input("Answer: ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_answer):
				print "Is not a number!"
			elif len(userinput_answer.strip()) == 0 :
				print "No input"	
			elif userinput_answer in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try again"
			else:
				break
		userinput_answerToint = int(userinput_answer)
		if userinput_answerToint != operation:
			print "oops"
			print
			print
			wrong_int.append(operation)
			wrong_str.append(operation2)

	total_entered = len(lista)
	total_wrong = len(wrong_str)
	#total = int(total_entered)- int(total_wrong)
	userinput_maxoperations_int = int(userinput_maxoperations)
	wrong_str_lenght = len(wrong_str)
	total = userinput_maxoperations_int - wrong_str_lenght
	print "Calculating..."
	time.sleep(3)
	print "=================================================================="
	print "You got ", total , " out of ", userinput_maxoperations, " CORRECT!"
	print "------------------"
	print "Summary.... "
	time.sleep(2)
	print "Incorrect operations!"
	for lista_incorrecta in wrong_str:
		print lista_incorrecta
	print "Only : ",len(wrong_str)
	if len(wrong_str) == 0 :
		print "Congrats... You are done"
		time.sleep(2)
		os.system('clear')
	else:
		print	
		print
		print
		print "------------------------"
		time.sleep(5)
		os.system('clear')
		print "Let's try again with the ones you got incorrect: "
		##Function to to redo the incorrect ones
		def tryingagain():
			while True: 
				userinput_tryagain = raw_input("Answer: ")
				if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain):
					print "Is not a number!"
				elif len(userinput_tryagain.strip()) == 0 :
					print "No input"
				elif userinput_tryagain in [',','<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
					print "Try again"
				else:
					break
			userinput_tryagain_int = int(userinput_tryagain)
			if userinput_tryagain_int != int(wrong_int_index):
				print "oops"
				print
				print
				two_wrong_str_list.append(wrong_str_index)
				two_wrong_int_list.append(wrong_int_index)
		i=0
		c=0 
		while i< total_wrong:
			wrong_str_index = str(wrong_str[i])
			wrong_int_index = str(wrong_int[c])
			print str(wrong_str[i])
			tryingagain()
			i+=1
			c+=1

		if len(two_wrong_str_list) == 0 :
			print "Congrats.... You are done"
			time.sleep(2)
			os.system('clear')
		else:
			print "Calculating...."
			time.sleep(5)
			os.system('clear')
			print "===================================="
			print "Incorrect operations:"
			print "-------"
			iii=0
			ccc=0
			for juniper in two_wrong_str_list:
				wrong_str_index = (two_wrong_str_list[iii])
				wrong_int_index = (two_wrong_int_list[ccc])
				print wrong_str_index
				iii+=1
				ccc+=1
			print
			print
			print
			print "You are almost done - Lets review the ones you still got incorrect!"
			ii=0
			cc=0
			total_wrong2 = len(two_wrong_str_list)

			while ii< total_wrong2:
				wrong_str_index2 = str(two_wrong_str_list[ii])
				wrong_int_index2 = str(two_wrong_int_list[cc])
				print wrong_str_index2
				invalid = True
				while invalid:
					userinput_tryagain1 = raw_input("Answer: ")
					if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain1):
						print "Is not a number!"
					elif len(userinput_tryagain1.strip()) == 0 :
						print "No input"
					elif userinput_tryagain1 == wrong_int_index2:
						print ("Good!")
						invalid = False
					else: 
						print ("try again")
						print
						print
						
				ii+=1
				cc+=1
			print ("You are now done!")
			os.system('clear')


def divisionz(userinput_maxoperations):

	i = datetime.now()
	e = i.strftime('%H:%M:%S')

	os.system('clear')
	quit = "0"
	lista = list()
	wrong_str = list()
	wrong_int = list()
	two_wrong_str_list = list()
	two_wrong_int_list = list()
	two_lista = list()
	print """
	**********************************************************
			READ BEFORE PROCEEDING!!!!!

		***********************************
		*	Round to the NEAREST 10   *
		***********************************


	For example:
	89 / 9 = 9

	The nearest 10 could be either 80 or 90 , right?

	** The correct answer is 9

	That is because 9 * 9 is equals to 81 which is the nearest 10 to 89 is 90

	**********************************************************
	"""
	print 
	print 

	enteruser = raw_input("Press ENTER to continue")


	#For loop to do math - 
	for line in range(int(userinput_maxoperations)):
		a = randint(1,90)
		b = randint(2,9)
		operation = a / b
		operation2 = str(a) + " / " + str(b) + ":"
		print operation2

		while True: 
			userinput_answer = raw_input("Answer: ")
			if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_answer):
				print "Is not a number!"
			elif len(userinput_answer.strip()) == 0 :
				print "No input"
			elif userinput_answer in ['<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
				print "Try again"
			else:
				break
		userinput_answerToint = int(userinput_answer)
		if userinput_answerToint != operation:
			print "oops"
			print
			print
			wrong_int.append(operation)
			wrong_str.append(operation2)

	total_entered = len(lista)
	total_wrong = len(wrong_str)
	#total = int(total_entered)- int(total_wrong)
	userinput_maxoperations_int = int(userinput_maxoperations)
	wrong_str_lenght = len(wrong_str)
	total = userinput_maxoperations_int - wrong_str_lenght
	print "Calculating..."
	time.sleep(3)
	print "=================================================================="
	print "You got ", total , " out of ", userinput_maxoperations, " CORRECT!"
	print "------------------"
	print "Summary.... "
	time.sleep(2)
	print "Incorrect operations!"
	for lista_incorrecta in wrong_str:
		print lista_incorrecta
	print "Only : ",len(wrong_str)
	if len(wrong_str) == 0 :
		print "Congrats... You are done"
		time.sleep(2)
	else:
		print	
		print
		print
		print "------------------------"
		time.sleep(5)
		os.system('clear')
		print "Let's try again with the ones you got incorrect: "
		##Function to to redo the incorrect ones
		def tryingagain():
			while True: 
				userinput_tryagain = raw_input("Answer: ")
				if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain):
					print "Is not a number!"
				elif len(userinput_tryagain.strip()) == 0 :
					print "No input"
				elif userinput_tryagain in ['<','@','!','~','#','$','%','^','&','*','-','_','=','+','?','>',',','.','/','`',':',';',"'"]:
					print "Try again"
				else:
					break
			userinput_tryagain_int = int(userinput_tryagain)
			if userinput_tryagain_int != int(wrong_int_index):
				print "oops"
				print
				print
				two_wrong_str_list.append(wrong_str_index)
				two_wrong_int_list.append(wrong_int_index)
		i=0
		c=0 
		while i< total_wrong:
			wrong_str_index = str(wrong_str[i])
			wrong_int_index = str(wrong_int[c])
			print str(wrong_str[i])
			tryingagain()
			i+=1
			c+=1
		if len(two_wrong_str_list) == 0 :
			print "Congrats.... You are done"
			time.sleep(2)
			os.system('clear')
		else:
			print "Calculating...."
			time.sleep(5)
			os.system('clear')
			print "===================================="
			print "Incorrect operations:"
			print "-------"
			iii=0
			ccc=0
			for juniper in two_wrong_str_list:
				wrong_str_index = (two_wrong_str_list[iii])
				wrong_int_index = (two_wrong_int_list[ccc])
				print wrong_str_index
				iii+=1
				ccc+=1
			print
			print
			print
			print "You are almost done - Lets review the ones you still got incorrect!"
			ii=0
			cc=0
			total_wrong2 = len(two_wrong_str_list)

			while ii< total_wrong2:
				wrong_str_index2 = str(two_wrong_str_list[ii])
				wrong_int_index2 = str(two_wrong_int_list[cc])
				print wrong_str_index2
				invalid = True
				while invalid:
					userinput_tryagain1 = raw_input("Answer: ")
					if re.search(r'(\w+[a-z]|\w+[A-Z])',userinput_tryagain1):
						print "Is not a number!"
					elif len(userinput_tryagain1.strip()) == 0 :
						print "No input"
					elif userinput_tryagain1 == wrong_int_index2:
						print ("Good!")
						invalid = False
					else: 
						print ("try again")
						print
						print
						
				ii+=1
				cc+=1
			print ("You are now done!")








print "Multiplication "
print '**********'
time.sleep(1)
multiplicationz(userinput_maxoperations)
print 
print
print "Subtracting  "
print "Get READY!!"
print "**********"
time.sleep(1)
press_enter=raw_input("Press Enter to continue")
subtractingz(userinput_maxoperations)
print
print
print "Adding "
print "Get READY!!"
print "***********"
time.sleep(1)
press_enter=raw_input("Press Enter to continue")
addingz(userinput_maxoperations)
print
print
print "Division "
print "Get READY!!"
print "***********"
time.sleep(1)
press_enter=raw_input("Press Enter to continue")
divisionz(userinput_maxoperations)



