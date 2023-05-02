from flask.globals import request
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from project_orm import User

from flask import Flask,session,flash,redirect,render_template,url_for

app = Flask(__name__)
app.secret_key = "the basics of life with python"


def get_db():
    engine = create_engine('sqlite:///database\\\\\\\\\\\.db')
    Session = scoped_session(sessionmaker(bind=engine))
    return Session()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and email(email):
            if password and len(password)>=6:
                try:
                    sess = get_db()
                    user = sess.query(User).filter_by(email=email,password=password).first()
                    if user:
                        session['isauth'] = True
                        session['email'] = user.email
                        session['id'] = user.id
                        session['name'] = user.name
                        session['created_at']=user.created_at
                        del sess
                        flash('hurray! Login successfull.','success')
                        return redirect('/home')
                    else:
                        flash('sorry!email or password is wrong.','danger')
                except Exception as e:
                    flash(e,'danger')
    return render_template('login.html',title='login')

@app.route('/signup',methods=['GET','POST'])
def signup():
   
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        if name and len(name) >= 3:
            if email and email(email):
                if password and len(password)>=6:
                    if cpassword and cpassword == password:
                        try:
                            sess = get_db()
                            newuser = User(name=name,email=email,password=password)
                            sess.add(newuser)
                            sess.commit()
                            del sess
                            flash('hurray!registration successful.','success')
                            return redirect('/')
                        except:
                            flash('*email account already exists','danger')
                    else:
                        flash('*Sorry!confirm password does not match','danger')
                else:
                    flash('*password must be of more than 6 characters.','danger')
            else:
                flash('*invalid email!','danger')
        else:
            flash('*invalid name! must be more than 3 characters.','danger')
    return render_template('signup.html',title='register')

@app.route('/forgot',methods=['GET','POST'])
def forgot():
    return render_template('forgot.html',title='forgot password')

@app.route('/home',methods=['GET','POST'])
def home():
    if session.get('isauth'):
        username = session.get('name')
        return render_template('upload.html',title=f'Home|{username}')
    else :
         return render_template('home.html')
   

@app.route('/about')
def about():
    return render_template('about.html',title='About Us')

@app.route('/login/profile')

def profile():

    return render_template('/profile.html')

@app.route('/logout')
def logout():
    if session.get('isauth'):
        session.clear()
        flash('you have been logged out','warning')
    return redirect('/login')

@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True,threaded=True)

