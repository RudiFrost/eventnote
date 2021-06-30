import sqlite3


def record_note(word):
    a = word.split(' ')
    title = a[1]
    descr = a[-1]
    con = sqlite3.connect("eventnote.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO notes (title, description)
                         VALUES (?, ?)""", (title, descr)).fetchall()
    con.commit()
