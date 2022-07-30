from workflowmanager import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), unique=True, nullable=False)
    contact_no = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    tasks = db.relationship("Task", backref="company", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.company_name

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.String(25), nullable=False)
    materials = db.Column(db.String(25), nullable=False)
    printing = db.Column(db.String(25), nullable=False)
    finishing = db.Column(db.String(25), nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    delivery_address = db.Column(db.String(50), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"