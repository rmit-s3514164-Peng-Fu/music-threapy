import os
from flask import Flask, render_template, request,redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager

from flask.ext.heroku import Heroku


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mvhctbhnyjqbph:gCuRtzxvVNUycilGrDD2GIFjv9@ec2-54-235-78-240.compute-1.amazonaws.com:5432/d1tbu4993m5g5p'
heroku = Heroku(app)
db = SQLAlchemy(app)
manager = Manager(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    def __init__(self, username,password):
        self.username = username
        self.password = password

    def __repr__(self,self):
        return '<username %r password %r>' % self.username %self.password

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not db.session.query(User).filter(User.username == username).count():
            reg = User(username,password)
            db.session.add(reg)
            db.session.commit()
        else:
            return 'username already used'
        return render_template('success.html')
    return render_template('signup.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.session.query(User).filter(User.username == username).count() > 0:
            return render_template('success.html')
        else :
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

# Save e-mail to database and send to success page
#@app.route('/prereg', methods=['POST'])
#def prereg():
#    email = None
#    if request.method == 'POST':
#        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
#        if not db.session.query(User).filter(User.email == email).count():
#            reg = User(email)
#            db.session.add(reg)
#            db.session.commit()
#            return render_template('success.html')
#    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()
