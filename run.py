from meuapp import app
from meuapp import manager
from meuapp.models import tables
from meuapp.models.tables import Login
from meuapp.models.form import MyForm
from meuapp import db
from flask import render_template, redirect


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/habilidades")
def habilidades():
    return render_template('habilidades.html')

@app.route("/cadastrar_livro")
def cadastrar_livro():
    return render_template('cadastrar_livro.html')

#@app.route('/teste',methods=['GET','POST'])
#def teste():
	
	#return render_template('teste.html',usuarios=usuarios)

@app.route('/teste', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    usuarios=Login.query.all()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('teste.html', usuarios=usuarios,form=form)


#i=Login('dougladd2s','adfddads12345')
#db.session.add(i)
#db.session.commit()


if __name__=='__main__':
	manager.run()
	#db.create_all()