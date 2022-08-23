import  sqlite3

conn  =  sqlite3.connect( 'data/data_sql.db' )
cur  =  conn.cursor ()
#create the salesman table 
# cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")

# cur.execute("""
# INSERT INTO weapon_types (id, name)
# VALUES (4, 'Legend')
# """)
sw = cur.execute("""
SELECT * FROM weapon_types
""")

conn.commit ()
print ( 'Data entered successfully.' )
print(sw)
rows = cur.fetchall()
conn . close ()

if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")
