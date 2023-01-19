from flask import Flask
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Import custom modules.
import forms

# Import blueprints.
from manage import * 


# Register blueprints.
app.register_blueprint(bp_conversation)
app.register_blueprint(bp_conversation_add)
app.register_blueprint(bp_conversation_import)


if __name__ == "__main__":
	app.run(debug=True, port=5000)