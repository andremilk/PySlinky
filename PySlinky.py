from flask import Flask, render_template
import sys
import subprocess
from load_stress import main, get_health
import netifaces as ni

ip = ni.ifaddresses('eth0')[2][0]['addr']
app = Flask(__name__)

@app.route('/load')
@app.route('/load/')
@app.route('/load/<string:expression>', methods=['GET'])
def load_stress(expression='x**x'):
    main(expression)
    return ip

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001, threaded=True)
