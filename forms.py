from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

# Class for conversation form.
class ConversationForm(FlaskForm):
	name = StringField(
			'Name*',
			[DataRequired()]
	)
	submit = SubmitField('Add conversation')


# Class for upload form.
class ConversationUpload(FlaskForm):
	chat = FileField(
		"File",
		[DataRequired()]
	)
	conv = SelectField(
		"Conversation",
		[DataRequired()],
		coerce=int,
	)
	submit = SubmitField('Import conversation')