from flask import Flask, request, render_template
from main import interpret_text
app = Flask(__name__, template_folder='templates')


@app.route('/')
def my_form():
    return render_template('textbox.html')


@app.route('/getValueFromTextbox', methods=['POST'])
def get_value():
    value = request.form['text']
    interpret_text(value)
    return render_template('textbox.html')
