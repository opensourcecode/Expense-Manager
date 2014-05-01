# Database logic goes here
# A user database is to be created and methods have to be defined
# so as to register a new user and provide login for other users.
# The database used here is MySQL though personally i would have
# preferred MongoDB.


import MySQLdb as mdb

#################################################################################################################################

def add_expense(username, description, xdate, category, amount, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "INSERT INTO expenses(username, description, xdate, category, amount) VALUES ('%s', '%s', '%d', '%s', '%f')" %(username, description, xdate, category, amount)
	cursor.execute(query)
	db.commit()
	db.close()

#################################################################################################################################

def get_expenses_by_month(fromDate, toDate, username, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT * FROM expenses WHERE xdate >= '%d' AND xdate < '%d' AND username = '%s'" %(fromDate, toDate, username)
	#print "query = ", query
	cursor.execute(query)
	db.commit()
	result = cursor.fetchall()
	db.close()
	#print "result = ",result
	return result

#################################################################################################################################

def get_expenses_by_year_category(fromDate, toDate, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT category, sum(amount) FROM expenses WHERE xdate >= '%d' AND xdate <= '%d' AND username = '%s' GROUP BY category" %(fromDate, toDate, username)
	cursor.execute(query)
	result = cursor.fetchall()
	db.close()
	return result

#################################################################################################################################

def get_expenses_by_year_months(fromDate, toDate, username, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT xdate, sum(amount) FROM expenses WHERE xdate >= '%d' AND xdate <= '%d' AND username = '%s' GROUP BY xdate" %(fromDate, toDate, username)
	cursor.execute(query)
	result = cursor.fetchall()
	db.close()
	return result


#################################################################################################################################

def get_expenses_for_a_period(start, end, username, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT * FROM expenses WHERE xdate >= '%d' AND xdate <= '%d' AND username = '%s'" %(start, end,username)
	cursor.execute(query)
	db.commit()
	result = cursor.fetchall()
	db.close()
	return result

#################################################################################################################################

def get_category_total_for_a_period(start, end, username, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT category, sum(amount) FROM expenses WHERE xdate >= '%d' AND xdate < '%d' AND username = '%s' GROUP BY category" %(start, end, username)
	cursor.execute(query)
	result = cursor.fetchall()
	db.close()
	return result
	

#################################################################################################################################

def authenticate_user(username, password, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "SELECT password FROM user WHERE username = '%s'" %(username)
	cursor.execute(query)
	db.commit()
	result = cursor.fetchall()
	db.close()

	if not cursor.rowcount:
		print "User does not exist!"
		return False
	else:
		x = result[0][0]

		if x == password:
			return True
		else:
			return False


#################################################################################################################################

def create_new_user(username, password, email, db_name = 'expensemanager'):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query = "INSERT INTO user VALUES ('%s', '%s', '%s')" %(username, password, email)
	cursor.execute(query)
	db.commit()
	db.close()
	

#################################################################################################################################