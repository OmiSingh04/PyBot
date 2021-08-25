import mysql.connector
from datetime import datetime
import logging
class Db_Manager:


	def __init__(self, user, password, database):
		self.database = database
		self.user = user
		self.password = password
		self.connector = mysql.connector
		self.connection =  self.connector.connect(host='localhost', database=database, user=user,password=password, buffered=True)
		if self.connection.is_connected():
			print('Connected to MySQL database')


	def reconnect(self):
		self.connection = mysql.connector.connect(host='localhost', database=self.database, user=self.user,password=self.password, buffered=True)
		print("Reconnected")

	def set_query(self, sql, val):
		try:
			cursor = self.connection.cursor()
			cursor.execute(sql, val)
			self.connection.commit()
			cursor.close()
			return "t"
		except (self.connector.Error) as e:
			self.log_error(e)
			return 'f'

	def get_query(self, sql, val):		
		try:
			cursor = self.connection.cursor()
			cursor.execute(sql, val)
			self.connection.commit()
			rs =  cursor.fetchall()
			cursor.close()
			return rs
		except (self.connector.Error) as e:
			self.log_error(e)
			return 'err'


	def log_error(self, e):
		now = datetime.now()
		date_string = now.strftime("%d/%m/%Y %H:%M:%S")
		f = open('..\\error_log.txt', 'a')
		f.write(str(e) + "\n" + f"{date_string}" + "\n\n\n")


	def is_registered(self, user_id):
		try:
			sql = "SELECT ID FROM USERS WHERE ID = %s"
			val = (str(user_id),)
			cursor = self.connection.cursor()
			cursor.execute(sql, val)
			rs =  cursor.fetchall()
			return True if len(rs) > 0 else False
		except (self.connector.Error) as e:
			self.log_error(e)
			return 'err'
		


	def register(self, user_id):
		if not self.is_registered(user_id):
			cursor = self.connection.cursor()
			sql = '''INSERT INTO USERS VALUES(%s, %s, %s)'''
			val = (str(user_id), 500, 1,)
			cursor.execute(sql,val)
			self.connection.commit()
			cursor.close()
			return True
		return False

	def get_coins(self, user_id):
		if not self.is_registered(user_id):
			return 'n_r'
		rs = self.get_query("SELECT COINS FROM USERS WHERE ID = %s", (str(user_id),))
		return rs[0][0] if type(rs) == list else rs

	def set_coins(self, user_id, coins):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET COINS = %s WHERE ID = %s", (coins, str(user_id),))

	def add_coins(self, user_id, coins):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET COINS = COINS + %s WHERE ID =%s", (coins, str(user_id),)) 

	def sub_coins(self, user_id, coins):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET COINS = COINS - %s WHERE ID = %s", (coins, str(user_id),))


	def set_level(self, user_id, level):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET LEVELS = %s WHERE ID = %s", (level, str(user_id),))	

	def get_level(self, user_id):
		if not self.is_registered(user_id):
			return 'n_r'
		rs =  self.get_query("SELECT LEVELS FROM USERS WHERE ID = %s",(str(user_id),))
		return rs[0][0] if type(rs) == list else rs

	def add_level(self, user_id, level):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET LEVELS = LEVELS + %s WHERE ID = %s",(level, str(user_id),))

	def sub_level(self, user_id, level):
		if not self.is_registered(user_id):
			return 'n_r'
		return self.set_query("UPDATE USERS SET LEVELS = LEVELS - %s WHERE ID = %s",(level, str(user_id),))
