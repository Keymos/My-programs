from flask import render_template, url_for, flash, redirect, request, jsonify
from flaskblog import app, db
from flaskblog.models import Task
from flaskblog.forms import RegistrationForm, LoginForm

#@app.errorhandler(404)

@app.route('/')
@app.route('/home')
def home():
    todo_list = db.session.query(Task).all()
    return render_template("General.html", todo_list=todo_list)


@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")
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