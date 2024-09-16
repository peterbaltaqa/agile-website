from flask import Flask, render_template, request, redirect, url_for, session
from auth import auth
from db import table


app = Flask(__name__)
app.secret_key = '4d807908c92fd04afceb10f7dc461f98ae6bbcc9c5dfb13fd7f9e0502fdf5968'

# Index Page
@app.route("/")
def index(): 
    if 'usr' in session:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))

# Home Page
@app.route("/home", methods=["GET", "POST"])
def home():
    if 'usr' in session:
        if request.method == 'GET':
            return render_template("home.html", table = table())
        
        elif request.form.get("edit") is not None:
            return render_template("home.html", table = table(), mode = "edit")
        
        elif request.form.get("save") is not None:
            return render_template("home.html", table = table(), mode = "save")
        
        elif request.form.get("add") is not None:
            pass

        elif request.form.get("delete") is not None:
            pass

    else:
        return redirect(url_for('login'))


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    session.pop('usr', None)

    if request.method == 'GET':
        return render_template("login.html")
    
    else:
        usr = request.form["usr"]
        pw = request.form["pw"]

        if not auth(usr, pw):
            return render_template("login.html", loginfail = True)
        else:
            session['usr'] = usr
            return redirect(url_for('home'))


    