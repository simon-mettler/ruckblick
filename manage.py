from flask import Blueprint, render_template, request
import sqlite3 as sql
import forms
import query
import inc


# Initialize blueprints.
manage_conversations = Blueprint('manage_conversations', __name__)
manage_conversation = Blueprint('manage_conversation_form', __name__)
manage_conversation_import = Blueprint('manage_conversation_form_import', __name__)


@manage_conversations.route("/manage/conversation/", methods=['GET', 'POST'])
@manage_conversation_import.route("/manage/conversation/<int:id>/", methods=['GET', 'POST'])
def m_conversation_import(id=None):
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

    return render_template("manage-conversation-import.html",
    form=form,
    id=id)


@manage_conversation.route("/manage/conversation/add/", methods=['GET', 'POST'])
def m_conversation_add():
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
        
    return render_template("manage-conversation-form.html", 
        form = form)