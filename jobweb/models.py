from _datetime import datetime
from jobweb import db

class Job(db.Model):
    stt = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(50))
    source_url = db.Column(db.String(200))
    import_datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_title = db.Column(db.String(200))
    company_title = db.Column(db.String(200))
    updated_date = db.Column(db.String(50))
    work_location = db.Column(db.String(200))
    category = db.Column(db.String(200))
    salary = db.Column(db.String(50))
    level = db.Column(db.String(50))
    deadline = db.Column(db.String(50))
    experience = db.Column(db.String(200))
    job_description = db.Column(db.Text)
    job_requirement = db.Column(db.Text)
    other_information = db.Column(db.Text)
    tags = db.Column(db.Text)

