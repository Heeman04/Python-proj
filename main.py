from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from model import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)
app.secret_key = "this is a secret key"

def get_db_session():
    engine = create_engine('sqlite:///project.sqlite')
    DBSession = sessionmaker(bind=engine)
    session = scoped_session(DBSession)
    return session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/add', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        db_session = get_db_session()
        user = User(name=name, email=email, password=hashed_password)
        db_session.add(user)
        db_session.commit()
        db_session.close()
        flash('User successfully created!')
        return redirect('/signup/add')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db_session = get_db_session()
        user = db_session.query(User).filter_by(email=email).first()
        if user is not None and check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.name
            db_session.close()
            return redirect("/")
        else:
            db_session.close()
            flash('Invalid email or password')
            return redirect('/login')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)