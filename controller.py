# This file contains the functions that would be exposed to the GUI

# TODO -- check if datepicker can be implemented using tkinter

import db
import md5
import datetime
import pyplots
import getpass
import texttable as tt

#######################################################################################################################

def add_entry(username):
	#username = raw_input()
	description = raw_input("Description : ")
	xdate = int("".join(raw_input("Date(yyyy-mm-dd) : ").split("-")))
	category = raw_input("Category : ")
	amount = float(raw_input("Amount : "))

	# add error checking for invalid date later
	# xxdate = datetime.date(xyear, xmonth, xdate)

	db.add_expense(username, description, xdate, category, amount)

#######################################################################################################################

def get_results_by_month(username):
	from_month = raw_input("Enter starting month (mm) : ")
	from_year = raw_input("Enter starting year (yyyy) : ")
	from_date = '00'
	fromDate = int(from_year + from_month +from_date)

	tm = input("Enter ending month (mm) : ") + 1
	if tm < 10:
		to_month = '0' + str(tm)
	else:
		to_month = str(tm)
	to_year = raw_input("Enter ending year (yyyy) : ")
	to_date = '00'
	toDate = int(to_year + to_month + to_date)

	result = db.get_expenses_by_month(fromDate, toDate, username)
	tab = tt.Texttable()

	head = ["ID", "USERNAME", "DESCRIPTION", "DATE", "CATEGORY", "AMOUNT"]
	

	x = []
	x.append(head)

	for i in xrange(len(result)):
		x.append(list(result[i]))

	tab.add_rows(x)
	tab.set_cols_align(['c', 'l', 'l', 'c', 'c', 'l'])
	#tab.header(head)
	print tab.draw()


	#choice = input("Press 1 and enter for pie chart, 2 for bar chart and any other number to move on")
	
	get_results_by_category_for_a_period(fromDate, toDate, username)

#######################################################################################################################

def get_results_for_a_period(username):
	fromDate = int("".join(raw_input("from Date(yyyy-mm-dd) : ").split("-")))
	toDate = int("".join(raw_input("to Date(yyyy-mm-dd) : ").split("-")))

	result = db.get_expenses_for_a_period(fromDate, toDate, username)
	
	tab = tt.Texttable()

	head = ["ID", "USERNAME", "DESCRIPTION", "DATE", "CATEGORY", "AMOUNT"]
	

	x = []
	x.append(head)

	for i in xrange(len(result)):
		x.append(list(result[i]))

	tab.add_rows(x)
	tab.set_cols_align(['c', 'l', 'l', 'c', 'c', 'l'])
	#tab.header(head)
	print tab.draw()


	get_results_by_category_for_a_period(fromDate, toDate, username)



#######################################################################################################################

def get_results_by_category_for_a_period(fromDate, toDate, username):
	#fromDate = int("".join(raw_input().split("-")))
	#toDate = int("".join(raw_input().split("-")))

	result = db.get_category_total_for_a_period(fromDate, toDate, username)

	tab = tt.Texttable()
	head = ["CATEGORY", "TOTAL AMOUNT"]
	

	x = []
	x.append(head)

	for i in xrange(len(result)):
		x.append(list(result[i]))

	tab.add_rows(x)
	tab.set_cols_align(['l', 'l'])
	#tab.header(head)
	print tab.draw()

	choice = input("Press 1 and enter for pie chart, 2 for bar chart and any other number to move on : ")

	xlist = []
	ylist = []

	for i in xrange(len(result)):
		xlist.append(result[i][0])
		ylist.append(result[i][1])

	if choice == 1:
		pyplots.draw_pie_chart(xlist, ylist)
	elif choice == 2:
		pyplots.draw_bar_chart_categories(xlist, ylist)

#######################################################################################################################

def register():
	username = raw_input("Username : ")
	password = getpass.getpass("Password : ")
	repeat_password = getpass.getpass("Repeat password : ")
	email = raw_input("Email : ")

	phash = md5.new(password).hexdigest()
	rphash = md5.new(repeat_password).hexdigest()

	if phash != rphash:
		print "Passwords dont match! Sorry..."
	else:
		db.create_new_user(username, phash, email)

#######################################################################################################################

def login():
	username = raw_input("Username : ")
	password = md5.new(getpass.getpass("Password : ")).hexdigest()

	result = db.authenticate_user(username, password)

	if result:
		print "Authentication successful!"
		print "Welcome", username, "!"
		return True, username
	else:
		print "Wrong username or password..."
		return False, username

#######################################################################################################################

def get_results_for_a_year(username):
	from_month = '00'
	from_year = raw_input("from Year(yyyy) : ")
	from_date = '00'
	fromDate = int(from_year + from_month +from_date)

	to_month = '00'
	to_year = str(input("to Year(yyyy) : ") + 1)
	to_date = '00'
	toDate = int(to_year + to_month + to_date)


	x = raw_input("Press 1 for expense by category and 2 for expense by months and anything else to skip : ")

	if x == '1':
		result = db.get_category_total_for_a_period(fromDate, toDate, username)

		tab = tt.Texttable()
		head = ["CATEGORY", "TOTAL AMOUNT"]
		x = []
		x.append(head)

		for i in xrange(len(result)):
			x.append(list(result[i]))

		tab.add_rows(x)
		tab.set_cols_align(['l', 'l'])
		print tab.draw()

		xlist = []
		ylist = []

		for i in xrange(len(result)):
			xlist.append(result[i][0])
			ylist.append(result[i][1])

		pyplots.draw_pie_chart(xlist, ylist)
		pyplots.draw_bar_chart_categories(xlist, ylist)

	elif x == '2':
		result = db.get_expenses_by_year_months(fromDate, toDate, username)
		xlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		ylist = [0] * 12

		for i in xrange(len(result)):
			index = int(str(result[i][0])[4:6]) - 1
			ylist[index] += result[i][1]

		tab = tt.Texttable()
		head = ["MONTH", "TOTAL EXPENDITURE"]
		x = []
		x.append(head)

		for i in xrange(len(xlist)):
			y = []
			y.append(xlist[i])
			y.append(ylist[i])
			x.append(y)

		tab.add_rows(x)
		tab.set_cols_align(['l','l'])
		print tab.draw()

		pyplots.draw_pie_chart(xlist, ylist)
		pyplots.draw_bar_chart_categories(xlist, ylist)

#######################################################################################################################		