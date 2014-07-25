import sqlite3, sys
#usage: 
#	$ python food_query.py "kcal >=200"

conn = sqlite3.connect('./Sample_Database/food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' %sys.argv[1]
print(query)

#query = 'SELECT * FROM food WHERE kcal >=200'
curs.execute(query)

names = [f[0] for f in curs.description]

for row in curs.fetchall():
	for pair in zip(names,row):
		print('%s:%s' %pair)
	print 
	
conn.close()
