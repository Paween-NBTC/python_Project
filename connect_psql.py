import psycopg2

#connect Database
con = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='12345678')

print(con)

cur=con.cursor()

cur.execute('select * from nso_mobile limit 5;')
print(cur.fetchall())

con.commit()
cur.close()
con.close()
