import sys,time,random

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0./90)
 
sprint('    Welcome to the Number Guessing Game!')

sprint("\n                                                 -Creⱥ†e∂by ☺Ɱąɾմƒ")
opt=input("\n Want to start the game? (y/n) : ")
if opt=="y":
	print("\n That's' great.  Let's start.")
	print("\n   1. Easy\n   2. Medium\n   3. Hard")
	option=int(input("\n Choose a level : "))
	
	
	count=0
	
	
	while count<2:
			
		if option==1:
			
			inp=int(input("\n Guess a number 0-10: "))
			num=random.randint(0,10)
			if inp==num:
				if count==0:
					print("\n Wow!!!.You have made it in your ",(count+1), "st attempt. You are a champ 🏆. Have a great day.")
				
				elif count==1:
					print("\n Wow !!!.You have made it in your ",(count+1),"nd attempt. You are a champ 🏆 .Have a great day.")
					
				break
			else:
				print("\n Oh! You have missed it. You should try again.\n Your magic number was : ", num)
				
				choice=input("\n Want to try again?(y/n) : ")
				if choice=="y":
					print("\n Great. Lets try again.")
					count+=1
					continue
				elif choice=="n":
					print("\n The game is terminated. And you have lost it.")
					break
				else:
					print("\n Invalid keyword!")
					
			
		elif option==2:
			inp=int(input("\n Guess a number 0-20 : "))
			num=random.randint(0,20)
			if inp==num:
				print("\n You have won this game. You are a champ 🏆. Have a great day.")
					
					
				break
				
			else:
				print("\n Oh! You have missed it. You should try again.\n Your magic number was : ", num)
				choice=input("\n Want to try again? (y/n) : ")
				if choice=="y":
					print("\n Great. Lets try again")
					count+=1
					continue
				elif choice=="n":
					print("\n Then the is finished. And you have lost it")
					break
				else:
					print("\n Invalid keyword!")
		
		elif option==3:
			inp=int(input("\n Guess a number 0-30 : "))
			num=random.randint(0,30)
			if inp==num:
				print("\n You have won the game. You are a champ 🏆. Have a great day.")
				break
			else:
				print("\n Oh! You have missed it. You should try again.\n Your magic number was : ", num)
				choice=input("\n Want to try again?(y/n) : ")
				if choice=="y":
					print("\n Great. Lets try again")
					count+=1
					continue
					
				elif choice=="n":
					print("\n The game is terminated. And you have lost it")
					break
				else:
					print("\n Invalid keyword!")
		else:
			print("\n Invalid keyword!")
			quit()
		
			
	p=str(option*10)
	if inp!=num and count==2:
		print("\n It's your last chance. Be careful this time.")

		inp=int(input("\n Guess the number if you can 0- "+p+ " : "))
		if inp==num:
			print("\n Congratulation! You have made this in the last breath! You are a champ 🏆!\n\n\n    Thanks for staying with us . Have a great day.")
		else:
			print("\n Oh you have lost this game this time!\n\n Your magic number was : ", num,"\n\n   Thanks for staying with us . Have a great day.")

	    

elif opt=="n":
	print("\n   Ok. We will play later. Have a great day.")
	
else:
	print("\n   Invalid keyword . Choose a right one.")
