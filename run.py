from meuapp import app
from meuapp import manager
from meuapp.models import tables
from meuapp.models.tables import Login
from meuapp import db
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/habilidades")
def habilidades():
    return render_template('habilidades.html')

@app.route('/teste',methods=['GET','POST'])
def teste():
	usuarios=Login.query.all()
	return render_template('teste.html',usuarios=usuarios)


#i=Login('dougladd2s','adfddads12345')
#db.session.add(i)
#db.session.commit()


if __name__=='__main__':
	manager.run()
	#db.create_all()