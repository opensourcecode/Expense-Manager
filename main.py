import db
import controller
import pyplots

print "Welcome to Expense Manager!"
print "1. Login"
print "2. New user. Register?"
print "3. Exit"

ch = input("your choice : ")

if ch == 1:
	b, user = controller.login()

	if b is True:
		print "FEATURE LIST:"
		print "1. ADD EXPENSES TO YOUR EXPENSE DATABASE"
		print "2. RETRIEVE EXPENSES FROM YOUR EXPENSE DATABASE"
		print "3. EXIT"

		ch1 = input("Your choice : ")

		while ch1 != 3:
			if ch1 == 1:
				controller.add_entry(user)
				print "The expense added successfully"
			elif ch1 == 2:
				print "SUB-MENU:"
				print "1. GET EXPENSES FOR MONTHS"
				print "2. GET EXPENSES FOR A YEAR"
				print "3. GET EXPENSES FOR A PERIOD"

				ch2 = input("Enter your choice : ")

				if ch2 == 1:
					controller.get_results_by_month(user)
				elif ch2 == 2:
					controller.get_results_for_a_year(user)
				elif ch2 == 3:
					controller.get_results_for_a_period(user)
				else:
					print "Don't be a smartass! Just choose from the options provided!"
			else:
				print "Don't be a smartass! Just choose from the options provided!"

			ch4 = raw_input("Do you wanna continue(y/n)? ")

			if ch4 != 'y' and ch4 != 'Y':
				break

			ch1 = input("Your choice : ")
	else:
		print "Login failed! Try again later..."
elif ch == 2:
	controller.register()
elif ch == 3:
	print "Quitting...\n Bye!"
else:
	print "Don't be a smartass! Just choose from the options provided!"
