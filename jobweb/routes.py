from flask import render_template, url_for, request, flash, redirect
from jobweb import app
from jobweb.models import Job
from sqlalchemy import and_, or_, not_
from jobweb.forms import SearchForm

@app.route("/", methods=['GET', 'POST'])
def home():
    jobs = Job.query.order_by(Job.import_datetime.desc()).all()
    return render_template("home.html", title='Home Page', jobs=jobs)

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        jobs = Job.query.filter(
            or_(
                Job.tags.ilike("%" + request.form['search'] + "%"),
                Job.job_title.ilike("%" + request.form['search'] + "%"),
                Job.work_location.ilike("%" + request.form['search'] + "%"),
            )
        ).all()
        return render_template("search_results.html", jobs=jobs)
    jobs = Job.query.order_by(Job.import_datetime.desc()).all()
    return render_template("home.html", title='Home Page', jobs=jobs)

@app.route("/jobs")
def jobs():
    page = request.args.get('page', default=1, type=int)
    jobs = Job.query.order_by(Job.import_datetime.desc()).paginate(page=page, per_page=10)
    return render_template("jobs.html", jobs=jobs)

@app.route("/about")
def about():
    return render_template("about.html", title='About')



@app.route("/job/<int:job_id>")
def job(job_id):
    job = Job.query.get(job_id)
    return render_template("job.html", title=job.job_title, job=job)



