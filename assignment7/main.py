from flask import Flask, render_template
from Flask-WTF import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
@app.route('/')
def member():
    return render_template('member.html')


@app.route('/', methods=["POST"])
def register():
    return 'Success'


if __name__ == "__main__":
    app.run()
