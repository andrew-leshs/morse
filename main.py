import logging
import time
import webbrowser

from pyfiglet import Figlet

from logic import Logic
from flask import Flask, render_template, request
from turbo_flask import Turbo
import sqlite3 as sl

code = ""
de = ""

app = Flask(__name__)
obj = Logic()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", code=code, de=de)


@app.route('/encode', methods=['GET', 'POST'])
def encode():
    global code
    response = request.args.get("q")
    code = Logic.encode_to_morse(response)
    print(code)
    return "nothing"


@app.route('/decode')
def decode():
    global de
    response = request.args.get("q")
    de = Logic.decode_from_morse(response)
    return "nothing"


if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    text = Figlet(font="digital")
    print(text.renderText("MORSE"))
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")
    app.run()
