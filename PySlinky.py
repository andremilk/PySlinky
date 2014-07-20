from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
def load_stress():
    pass

@app.route('/db_entry')
def db_stress():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
