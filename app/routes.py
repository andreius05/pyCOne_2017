from app import app,bcrypt,db
from flask import render_template,redirect,url_for,flash
from app.forms import RegisterForm,LoginForm
from app.models import User
from flask_login import current_user,login_user

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegisterForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data)
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form,title='Register')



@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash('Your logged in an account','success')
            return redirect(url_for('name',username=user.username))
        return redirect(url_for('login'))
    return render_template('login.html',form=form)


@app.route('/name/<username>')
def name(username):
    return f"Hello {username}"