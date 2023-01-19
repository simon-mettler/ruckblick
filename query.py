import sqlite3 as sql

def get_conversations():
    con = sql.connect('data/chats.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM conversation")
    data = cur.fetchall()
    con.close()
    return data 