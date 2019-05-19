import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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
df.head()
df.info()
df.describe()
df.columns
X =df[['volume']]
y=df[['open','high','low','close']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
lm = LinearRegression()
lm.fit(X_train,y_train)
predictions = lm.predict(X_test)
print(predictions)
