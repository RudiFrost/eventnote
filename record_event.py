import sqlite3
from datetime import datetime


def record_event(word):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d.%m.%Y")
    a = word.split('  ')
    title = a[1]
    descr = a[2]
    date = a[-2].split('.')
    time = a[-1].split(':')
    notify = str(date[0]) + "." + str(date[1]) + "." + str(date[2]) + " " + str(time[0]) + ":" + str(
        time[-1]) + ":" + "00"
    con = sqlite3.connect("eventnote.db")
    cur = con.cursor()
    cur.execute(
        """INSERT INTO events (date, time, title, description, notify) 
        VALUES (?, ?, ?, ?, ?)""", (current_date, current_time, title, descr, notify)).fetchall()
    con.commit()
