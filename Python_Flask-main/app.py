from flask import Flask,render_template,request,redirect,session

from utils import hash_password
from models.user import User
from models.greenHouse import GreenHouse
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required

import requests
from extensions import db, jwt
from flask_migrate import Migrate
from config import Config
from resources import getplot


from utils import check_password

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

app = create_app()


@app.route('/home',methods=['POST','GET'])
def home():
    if 'username' in session:
        getplot("ducky@ducky.com")
        return render_template('home.html', msg = "Your are loggend in with email: " + session['username'], plot = "static/img/plot.png"  )



    else:
        return render_template('login.html',msg="Please Login First")


@app.route('/register',methods=['POST','GET'])
def register():
    return render_template('register.html')



@app.route('/add-users-to-db',methods=['POST','GET'])
def addUsers():
    if request.method == "POST":

        username = str(request.form['username'])
        email = str(request.form['email'])
        non_hash_password = str(request.form['password'])

        if username == "" or email == "" or non_hash_password == "":
            return render_template("register.html",msg="Ensure none of the fields are empty")
       
        else:
            password = hash_password(non_hash_password)
            
            jsondict = {}
            jsondict["email"] = email
            jsondict["password"] = password
            jsondict["username"] = username
            try:
                signup = requests.post('http://localhost:5000/users' ,
                                      headers= {'Content-Type': 'application/json'},
                                      json = jsondict)
                print("Message from the server:")
                print(signup)
                print()
            except requests.exceptions.RequestException as error:
                print("duck94859", error)            
   
            message = "User Has Been Added Successfully"
            return render_template("info.html",msg=message)
                
    else:
        #we redirect the user to the login page
        return redirect('/register')
    


@app.route('/',methods=['POST','GET'])
def login():
    
    if 'username' in session:
        
        return render_template('home.html', msg = "Your are loggend in with email: " + session['username'], plot = "static/img/plot.png" )

        
        
    else:
        return render_template('login.html',msg="Please Login First")


@app.route('/login-user',methods=['POST','GET'])
def loginUser():
    if request.method == "POST":
        #we check if the form has beed posted with empty fields
        email = str(request.form['email'])
        password = str(request.form['password'])
        user = User.get_by_email(email=email)
        
    
        if email == "" or password == "":
            return render_template("login.html",msg="Ensure that no field is empty")
        
        else:
            if not user or not check_password(password, user.password):
                return render_template("login.html",msg="The Email/Password Combination is Incorrect!")
                #...then we login the user by creating a sesssion.
            else:
                session['username'] = email
                return redirect('/home')

    else:
        return render_template("login.html",msg = "Wrong Request Method")

@app.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('username',None)
    return redirect('/')



if __name__ == "__main__":
    app.run(port=80, debug=True)