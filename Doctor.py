from flask import Flask, render_template
import sys
import subprocess
from load_stress import main, get_health
app = Flask(__name__)

@app.route('/health')
@app.route('/health/')
@app.route('/health/<int:now>', methods=['GET'])
def health(now=0):
    return str(get_health(now))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)
