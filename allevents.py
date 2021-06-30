import sqlite3


def print_events():
    a = []
    con = sqlite3.connect("eventnote.db")
    cur = con.cursor()
    result = cur.execute("""SELECT title ,notify FROM events""").fetchall()
    print(result)
    for i in range(len(result)):
        a.append(str(result[i])[2:-1])
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.replace(",", "\n")
    a = a.replace('"', "")
    return a
    con.close()