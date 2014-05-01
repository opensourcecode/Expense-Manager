import MySQLdb as mdb

#################################################################################################################################

def create_database(db_name):
	db = mdb.connect("localhost","root","")
	cursor = db.cursor()
	sql = "CREATE DATABASE IF NOT EXISTS %s" %(db_name)
	cursor.execute(sql)
	db.commit()
	db.close()

#################################################################################################################################

def create_tables(db_name):
	db = mdb.connect("localhost","root","",db_name)
	cursor = db.cursor()
	query1 = "CREATE TABLE IF NOT EXISTS user (username VARCHAR(100) PRIMARY KEY, password VARCHAR(100), email VARCHAR(100) unique)"
	cursor.execute(query1)
	query2 = "CREATE TABLE IF NOT EXISTS expenses (id INT NOT NULL AUTO_INCREMENT, username VARCHAR(100), description VARCHAR(100), xdate INT, category VARCHAR(20), amount REAL, PRIMARY KEY(id))"
	cursor.execute(query2)
	db.commit()
	db.close()

#################################################################################################################################

def initialize_database():
	db_name = "expensemanager"
	create_database(db_name)
	create_tables(db_name)


#################################################################################################################################

initialize_database()