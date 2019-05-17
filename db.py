import mysql.connector
conn = mysql.connector.connect(
         user='foouser',
         password='F88Pa%%**',
         host='134.209.144.239',
         database='stocksdb')
print(conn)
cur = conn.cursor()
cur.execute('SELECT * FROM interview')