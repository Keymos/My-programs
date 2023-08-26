from flask import render_template, url_for, flash, redirect, request, jsonify
from flaskblog import app, db
from flaskblog.models import Task
from flaskblog.forms import RegistrationForm, LoginForm
from datetime import datetime, timedelta, time

#@app.errorhandler(404)

@app.route('/')
@app.route('/home')
def home():
    todo_list = db.session.query(Task).all()

    # Calculate due_in and isDue for each task
    now = datetime.now()
    for todo in todo_list:
        if todo.date_due is not None:  # Check if date_due is not None
            todo.due_in = todo.date_due - now
            if todo.due_in.days < 0:
                todo.due_in = todo.date_due - now #- timedelta(days=1)
            todo.isDue = todo.due_in.total_seconds() <= 0

    time_0 = datetime.combine(datetime.today(),time(0, 0))
    return render_template("General.html", todo_list=todo_list, now=now, time_0=time_0)


@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")
    date_due_date = request.form.get("date_due_date")
    date_due_time = request.form.get("date_due_time")
    
    # Convert date_due_date and date_due_time to a single datetime object if provided
    date_due = None
    if date_due_date and date_due_time:
        date_due_str = f"{date_due_date} {date_due_time}"
        date_due = datetime.strptime(date_due_str, "%d/%m/%y %H:%M")
    elif date_due_time:  # Only time provided, check if not too late today
        current_datetime = datetime.now()
        date_due_str = f"{current_datetime.strftime('%d/%m/%y')} {date_due_time}"
        date_due = datetime.strptime(date_due_str, "%d/%m/%y %H:%M")
    elif date_due_date:  # Only date provided, set time to 00:00
        date_due_str = f"{date_due_date} 00:00"
        date_due = datetime.strptime(date_due_str, "%d/%m/%y %H:%M")
    
    if date_due is not None:
        new_task = Task(title=title, description=description, date_due=date_due)
    else:
        new_task = Task(title=title, description=description)
    
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    flash('Task has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/toggle_task_status/<int:task_id>', methods=['POST'])
def toggle_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json  # Retrieve the data sent in the JSON request
    if data and 'isDone' in data:
        task.isDone = data['isDone']
        db.session.commit()
    
    return jsonify(success=True)



@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are able now to log in!', "success")
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)