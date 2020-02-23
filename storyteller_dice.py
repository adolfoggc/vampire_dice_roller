import random

def roll_dice(dice, difficulty):
	success = 0
	count = 0
	while(count < dice):
		roll = random.randint(1,10)
		print(roll, end=" ")
		if(roll >= difficulty):
			success += 1
		elif(roll == 1):
			success -= 1
		count +=  1
	print("")
	if(success >= 1):
		print("Rolled", success, "success",end ="")
		if(success > 1):
			print("es")
		else:
			print("")
	elif(success == 0):
		print("Failure")
	else:
		print("Critical Failure!")

