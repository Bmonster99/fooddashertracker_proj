import sqlite3

def connect():
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dash (id INTEGER PRIMARY KEY, moneyBag integer, milesDriven integer, hoursWorked integer, dateText text)")
    conn.commit()
    conn.close()

def insert(moneyBag, milesDriven, hoursWorked, dateText):
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO dash VALUES (NULL, ?, ?, ?, ?)", (moneyBag, milesDriven, hoursWorked, dateText))
    conn.commit() # only needed when making changes to the database
    conn.close()

def view():
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dash")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(moneyBag = "", milesDriven = "", hoursWorked = "", dateText = ""):
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dash WHERE moneyBag =? OR milesDriven =? OR hoursWorked =? OR dateText =?", (moneyBag, milesDriven, hoursWorked, dateText))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM dash WHERE id = ?",(id,))
    conn.commit()
    conn.close()


def edit(id, moneyBag, milesDriven, hoursWorked, dateText):
    conn = sqlite3.connect("dashbe.db")
    cur = conn.cursor()
    cur.execute("UPDATE dash SET moneyBag = ?, milesDriven = ?, hoursWorked = ?, dataText = ? WHERE id = ?", (moneyBag, milesDriven, hoursWorked, dateText, id))
    conn.commit()
    conn.close()





connect()

insert(500, 100, 8, "2001-12-22")
print(view())
#print(search(dateText = "2001-12-21"))
        

    