import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_emotionclf_table():
	c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(Input_Text TEXT,Emotion TEXT,Score NUMBER,Time_of_Visit TIMESTAMP)')

def add_prediction_details(Input_Text,Emotion,Score,Time_of_Visit):
	c.execute('INSERT INTO emotionclfTable(Input_Text,Emotion,Score,Time_of_Visit) VALUES(?,?,?,?)',(Input_Text,Emotion,Score,Time_of_Visit))
	conn.commit()

def view_all_prediction_details():
	c.execute('SELECT * FROM emotionclfTable ORDER BY timeOfvisit DESC')
	data = c.fetchall()
	return data
