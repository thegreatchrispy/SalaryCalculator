import time
import sys
from os import system, name

# This function clears the terminal
def clear():
	# for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# This function prints out the introduction message, including assumptions
def printIntro():
	message = """
	This program will show you in real time how much you are earning.
	Assumptions made:
		* you are currently at work
		* 40 hour weeks (8 hour days)
		* overtime is not accounted for

	"""
	print(message)

# This function gets the salary from the user as input
def getSalary(message):
	while True:
		try:
			salary = int(input(message))
		except ValueError:
			print("Please enter an integer value...")
			continue
		else:
			return salary
			break

# This function calculates and updates the amount that you have earned in real time
def calculateCurrent(salary, start):
	perSecond = salary / 52.0 / 40.0 / 60.0 / 60.0
	print("Amount per second: $" + str(perSecond))
	earned = 0

	while True:
		current = int(time.time())
		earned += perSecond * (current - start)
		sys.stdout.write("Earned: " + '${:,.2f}'.format(earned) + '\r')
		sys.stdout.flush()
		time.sleep(1.0)

# Main program starts here
clear()
printIntro()
salary = getSalary("Enter your salary amount: $")
start = int(time.time())
calculateCurrent(salary, start)