from flask import render_template, flash, redirect,request
import sqlite3
import sys
from flask import g
from app import app
from .forms import LoginForm
from .forms import EnteryForm

@app.before_request
def before_request():
    g.db = sqlite3.connect("databook.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		username=form.openid.data
		pswd=form.password.data
		if username == 'loginuser' and pswd == 'password':
			flash('Login requested for OpenID=%s' % form.openid.data)
        		return redirect('/login')
		flash('Worng Username Or Password =%s' % form.openid.data)	
	return render_template('index.html',title='Home',form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EnteryForm()
    if form.validate_on_submit():
	name=form.student.data
	val=form.mark.data
	Std=(name,val)
	try:
		g.db.execute("CREATE TABLE IF NOT EXISTS student(name TEXT PRIMARY KEY,mark INT)")
	        nameval = g.db.execute("SELECT * FROM student").fetchall()
		nameval = g.db.execute("SELECT name FROM student").fetchall()
		if name not in nameval:
			g.db.execute("INSERT INTO student VALUES(?,?)",Std)
			g.db.commit()        
	except:
		pass
	
	finally:
		nameval = g.db.execute("SELECT * FROM Student").fetchall()
        	return render_template('login.html',nameval=nameval,title='Sign In',form=form)

    return render_template('login.html',title='Sign In',form=form)

@app.route('/record')
def record():
	nameval = g.db.execute("SELECT * FROM Student").fetchall()
	return render_template('record.html',title='Record',nameval=nameval)

@app.route('/project')
def project():
	return render_template("project.html",title='contact')
