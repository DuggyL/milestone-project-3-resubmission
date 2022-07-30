from flask import render_template
from workflowmanager import app, db
from workflowmanager.models import Company, Task

@app.route("/")
def home():
    return render_template("base.html")