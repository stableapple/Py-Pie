print("Choose: a= Rock, b= Scissor, c= Paper")
Player1= raw_input("Enter your choice Player 1: ")
Player2= raw_input("Enter your choice Player 2: ")
if Player1== "a":
	if Player2== "b":
		print("Player1 wins!!")
	elif Player2== "c":
		print("Player2 wins!!")
	else:
		print("Tie")
	print("Want to start a new game?")
if Player1== "b":
	if Player2== "c":
		print("Player1 wins!!")
	elif Player2== "a":
		print("Player2 wins!!")
	else:
		print("Tie")
	print("Want to start a new game?")
if Player1== "c":
	if Player2== "a":
		print("Player1 wins!!")
	elif Player2== "b":
		print("Player2 wins!!")
	else:
		print("Tie")
	print("Want to start a new game?")
else:
	print("Invalid input:)")
