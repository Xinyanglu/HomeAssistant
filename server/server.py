from flask import Flask, request, render_template
from flask_cors import CORS
import json
from server import functions

functions.setup_pins()

app = Flask(__name__)
CORS(app)


@app.route('/getValueFromLightSwitch', methods=['GET', 'POST'])
def get_value():
    value = json.loads(request.data)

    if value:
      functions.turn_desklight_on()
    else:
      functions.turn_desklight_off()
    return ("success")


if __name__ == '__main__':
    app.run(host='0.0.0.0')

