import sqlite3


def print_notes():
    a = []
    con = sqlite3.connect("eventnote.db")
    cur = con.cursor()
    result = cur.execute("""SELECT title FROM notes""").fetchall()
    for i in range(len(result)):
        a.append(str(result[i])[2:-3])
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.replace(",", "\n")
    a = a.replace(" ", "")
    return a
    con.close()
