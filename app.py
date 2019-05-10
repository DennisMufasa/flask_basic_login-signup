from flask import Flask, make_response, jsonify, session, request
from flask import render_template, flash, url_for, redirect
from flask_bcrypt import generate_password_hash, check_password_hash

import os

from data import User

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        e_mail = request.form['email']
        name = request.form['username']
        passwrd = generate_password_hash(request.form['password'])
        
        User.create(username=name, password=passwrd, email=e_mail)
        flash("New User added successfully!")
    return render_template('register.html')

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']

        try:
            user = User.get(User.username == name)
            if check_password_hash(user.password, password):
                # flash("Loggin Successful!")
                session['logged_in'] = True
                session['username'] = name
                return redirect(url_for('home'))
        except User.DoesNotExist:
            flash("Invalid username or password")
    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)