import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres", password="123456", host="localhost")
cursor = connection.cursor()
