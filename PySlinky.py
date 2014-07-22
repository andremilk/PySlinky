from flask import Flask, render_template
import sys
import subprocess
from load_stress import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
def load_stress(output=None):
    output = main('x**x')
    return render_template('load.html', output=output)

@app.route('/db_entry')
def db_stress():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
