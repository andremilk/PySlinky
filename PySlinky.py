from flask import Flask, render_template
import sys
import subprocess
from load_stress import main, get_health
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
@app.route('/load/')
@app.route('/load/<string:expression>', methods=['GET'])
def load_stress(expression='x**x'):
    output = main(expression)
    return str(output)

@app.route('/health')
@app.route('/health/')
@app.route('/health/<int:now>', methods=['GET'])
def health(now=0):
    return str(get_health(now))

@app.route('/db_entry')
def db_stress():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
