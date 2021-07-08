import mysql.connector

class Db_Manager:


	def __init__(self, user, password, database):
		self.connection =  mysql.connector.connect(host='localhost', database=database, user=user,password=password, buffered=True)
		if self.connection.is_connected():
			self.is_connected = True
			print('Connected to MySQL database')


	def is_registered(self, id):
		if not self.is_connected:
			return
		cursor = self.connection.cursor()
		sql = f"SELECT ID FROM users where ID = '{id}'"
		cursor.execute(sql)
		record = cursor.fetchall()
		if len(record) > 0:
			return True
		else:
			return False


	def register(self, id):
		if not self.is_connected:
			return
		if not self.is_registered(id):
			cursor = self.connection.cursor()
			sql = '''INSERT INTO USERS VALUES(%s, %s, %s)'''
			val = (id, 500, 1)
			cursor.execute(sql,val)
			self.connection.commit()
			print(cursor.rowcount, "record inserted.")
			cursor.close()
			return True
		return False
			