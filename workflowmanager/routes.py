from flask import render_template, request, redirect, url_for
from workflowmanager import app, db
from workflowmanager.models import Company, Task

@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/companies")
def companies():
    return render_template("companies.html")

@app.route("/add_company", methods=["GET", "POST"])
def add_company():
    companies = list(Company.query.order_by(Company.company_name).all())
    if request.method == "POST":
        company = Company(
            company_name=request.form.get("company_name"),
            contact_no=request.form.get("contact_no"),
            email=request.form.get("email"),
            address=request.form.get("address"),
        )
        db.session.add(company)
        db.session.commit()
        flash("Company Successfully added", category='success')
        return redirect(url_for("add_company"))
    return render_template("companies.html", companies=companies)
