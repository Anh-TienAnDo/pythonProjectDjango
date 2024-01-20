import mysql.connector

db = mysql.connector.connect(user='root', password='anh1710gdt', host='localhost', port='3306')
create_table = "CREATE DATABASE `TEST`"

cursor = db.cursor()
cursor.execute(create_table)

