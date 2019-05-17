import mysql.connector
import pandas as pd
def prune(syn):
    x=[]
    #print(syn)
    for i in range(2, len(syn) - 3):
        x.append(syn[i])

    return "".join(x)

conn = mysql.connector.connect(
         user='foouser',
         password='F88Pa%%**',
         host='134.209.144.239',
         database='stocksdb'
         )
#print(conn)
cur = conn.cursor()
cur.execute("SHOW TABLES")
tables = cur.fetchall()
for t in tables:
    t=prune(str(t))
    df=pd.read_sql_query("select * from "+t,conn)
    print(df)