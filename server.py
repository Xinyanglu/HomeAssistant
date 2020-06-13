from flask import Flask, request, render_template
import functions
functions.setup_pins()
app = Flask(__name__, template_folder='templates')


@app.route('/')
def my_form():
    return render_template('textbox.html')


@app.route('/getValueFromTextbox', methods=['POST'])
def get_value():
    value = request.form['text']
    functions.interpret_text(value)
    return render_template('textbox.html')
