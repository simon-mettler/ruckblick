import sqlite3 as sql

con = sql.connect("data/chats.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE "conversation" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
""")

cur.execute("""
CREATE TABLE "message" (
	"conversation"	INTEGER NOT NULL,
	"timestamp"	TEXT NOT NULL,
	"sender"	TEXT NOT NULL,
	"msg"	TEXT NOT NULL,
	FOREIGN KEY("conversation") REFERENCES "Conversation"("id"),
);
""")