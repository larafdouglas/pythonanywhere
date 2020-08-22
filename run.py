from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/habilidades")
def habilidades():
    return render_template('habilidades.html')


if __name__=='__main__':
	app.run()