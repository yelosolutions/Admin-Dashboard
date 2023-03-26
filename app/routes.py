from app import app
from flask import render_template, url_for

@app.route("/")
@app.route("/index")
def index():
    return render_template('dashboard.html', title='admin dashboard')

@app.route("/login")
def logout():
    return render_template("login.html")