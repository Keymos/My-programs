from flask import render_template, url_for, flash, redirect
#from flaskblog import app
#from flaskblog.forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    todo_list = db.session.query(Todo).all()
    return render_template("General.html", todo_list=todo_list)


@app.route("/add_task", methods=["POST"])
def add():
    title = request.form.get("title")
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit
    return redirect(url_for("home"))




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