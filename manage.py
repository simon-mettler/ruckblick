from flask import Blueprint, render_template, request
import sqlite3 as sql
import forms
import query
import inc


# Initialize blueprints.
bp_conversation = Blueprint('bp_conversation', __name__)
bp_conversation_add = Blueprint('bp_conversation_add', __name__)
bp_conversation_import = Blueprint('bp_conversation_import', __name__)


@bp_conversation.route("/conversation/")
def p_conversation():
    conversations = query.get_conversations()
    return render_template("conversation.html",
        conversations=conversations)


@bp_conversation_import.route("/conversation/import/", methods=['GET', 'POST'])
@bp_conversation_import.route("/conversation/import/<int:id>", methods=['GET', 'POST'])
def p_conversation_import(id=None):
    form = forms.ConversationUpload()
    form.conv.choices = [(c['id'], c['name']) for c in query.get_conversations()]
    if request.method == 'POST':
        file = request.files['chat']
        chat = file.read().decode("utf-8")

        con = sql.connect('data/chats.db')
        cur = con.cursor()
        print(form.conv.data)

        for msg in inc.chat_converter(chat):
            cur.execute('''
                INSERT INTO message (conv, timestamp, sender, msg) VALUES (?,?,?,?)
            ''', (form.conv.data, msg[0], msg[1], msg[2]))
            con.commit()
        con.close()
    form.conv.data = id

    return render_template("conversation-import.html",
    form=form,
    id=id)


@bp_conversation_add.route("/conversation/add/", methods=['GET', 'POST'])
def p_conversation_add():
    form = forms.ConversationForm()
    if form.validate_on_submit():
        name = form.name.data
        con = sql.connect('data/chats.db')
        cur = con.cursor()
        cur.execute('''
            INSERT INTO conversation
                (name)
            VALUES
                (?)
        ''', (name,))
        con.commit()
        con.close()
        
    return render_template("conversation-form.html", 
        form = form)