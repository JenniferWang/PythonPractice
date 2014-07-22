# use the data downloaded from http://www.ars.usda.gov/Services/docs.htm?docid=23634
# save the data with encoding utf-8
import sqlite3

def convert(value):
	if value.startswith('~'):
		return value.strip('~')
	if not value:
		value = '0'
	return float(value)

conn = sqlite3.connect('./Sample_Database/food.db')
curs =  conn.cursor()

curs.execute('''
CREATE TABLE food(
	id	TEXT	PRIMARY KEY,
	desc	TEXT,
	water	FLOAT,
	kcal	FLOAT,
	protein	FLOAT,
	fat 	FLOAT,
	ash 	FLOAT,
	carbs	FLOAT,
	fiber	FLOAT,
	sugar	FLOAT
   )
   ''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
with open('./Sample_Database/sr26abbr/ABBREV.txt') as f:
	for line in f:
		fields = line.split('^')
		vals = [convert(F) for F in fields[:10]]
		curs.execute(query,vals)

conn.commit()
conn.close()
