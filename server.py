from flask import Flask, request, render_template
import functions

functions.setup_pins()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def my_form():
    return render_template('Controls.html')


@app.route('/getValueFromLightSwitch', methods=['GET', 'POST'])
def get_value():
    value = request.form['status']
    if value == 'true':
        functions.turn_desklight_on()
    else:
        functions.turn_desklight_off()

    return "success"


if __name__ == '__main__':
    app.run()

