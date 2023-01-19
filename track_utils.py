import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_emotionclf_table():
	c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')

def add_prediction_details(rawtext,prediction,probability,timeOfvisit):
	c.execute('INSERT INTO emotionclfTable(rawtext,prediction,probability,timeOfvisit) VALUES(?,?,?,?)',(rawtext,prediction,probability,timeOfvisit))
	conn.commit()

def view_all_prediction_details():
	c.execute('SELECT * FROM emotionclfTable ORDER BY timeOfvisit DESC')
	data = c.fetchall()
	return data
