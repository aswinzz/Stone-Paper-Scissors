import random
import os
points=0
comppoints=0
cont=1
while(cont==1):
	userchoice = input("Rock,Paper or Scissors: ")
	computerchoice = random.randint(1,3)

	if(userchoice=="rock" or userchoice=="Rock" or userchoice=="ROCK"):
		userchoiceno=1
	elif(userchoice=="Paper" or userchoice=="PAPER" or userchoice=="paper"):
		userchoiceno=2
	elif(userchoice=="Scissors" or userchoice=="SCISSORS" or userchoice=="scissors"):
		userchoiceno=3
	else:
		print("Invalid Entry!!")
		continue

	if(computerchoice==1):
		print("Computer Choice is: Rock")
	elif(computerchoice==2):
		print("Computer Choice is: Paper")
	elif(computerchoice==3):
		print("Computer Choice is: Scissors")



	if(userchoiceno==computerchoice):
		print("its a tie")
	elif(userchoiceno==1 and computerchoice==2):
		print("Computer wins")
		if(points>0):
			points=points-1
		comppoints=comppoints+1
	elif(userchoiceno==1 and computerchoice==3):
		print("You win")
		points=points+1
		if(comppoints>0):
			comppoints=comppoints-1
	elif(userchoiceno==2 and computerchoice==1):
		print("You win")
		points=points+1
		if(comppoints>0):
			comppoints=comppoints-1
	elif(userchoiceno==2 and computerchoice==3):
		print("Computer wins")
		if(points>0):
			points=points-1
		comppoints=comppoints+1
	elif(userchoiceno==3 and computerchoice==1):
		print("Computer wins")
		if(points>0):
			points=points-1
		comppoints=comppoints+1
	elif(userchoiceno==3 and computerchoice==2):
		print("You win")
		points=points+1
		if(comppoints>0):
			comppoints=comppoints-1
	print("Your Current Score is : ",points)
	print("Computer's Current Score is : ",comppoints)
	x=int(input("To continue the game press 1 and to quit press 2 : "))
    
	if(x==2):
		break
	elif(x==1):
		continue
	else:
		print("invalid entry,Taking it as continue -_* ")
	os.system('clear') 