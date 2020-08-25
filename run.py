from meuapp import app
from meuapp import manager

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/habilidades")
def habilidades():
    return render_template('habilidades.html')


@app.route('/test/<info>')
@app.route('/test', defaults={'info':None})
def teste():
	i=User('douglas','douglas.laraf@gmail.com')
	db.session.add(i)
	db.session.commit()


if __name__=='__main__':
	manager.run()
	db.create_all()