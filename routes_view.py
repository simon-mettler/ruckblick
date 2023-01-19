from flask import Blueprint, render_template, request
import sqlite3 as sql
import inc
import query


bp_conversation_view = Blueprint('bp_conversation_view', __name__)

@bp_conversation_view.route("/conversation/view/<int:id>")
def p_conversation_view(id):
    conversations = query.get_conversations()
    con = sql.connect('data/chats.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM message WHERE conv = ?", (id,))
    messages = cur.fetchall()
    con.close()

    return render_template("conversation-view.html",
        conversations=conversations,
        messages=messages)