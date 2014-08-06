from flask import Flask, render_template
import sys
import subprocess
from load_stress import main, get_health
app = Flask(__name__)

@app.route('/load')
@app.route('/load/')
@app.route('/load/<string:expression>', methods=['GET'])
def load_stress(expression='x**x'):
    output = main(expression)
    return str(output)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001, threaded=True)
