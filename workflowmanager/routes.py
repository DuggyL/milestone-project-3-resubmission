from flask import render_template
from workflowmanager import app, db

@app.route("/")
def home():
    return render_template("base.html")