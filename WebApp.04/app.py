from flask import Flask #the application itself \
from flask import render_template #so we can work with html files\
from flask import request # so we can access the POST and FORM request data from html file\
from flask import redirect # so we can redirect from different endpoints\
from flask import url_for # allows to get urls dynamically
from os import listdir

app = Flask(__name__, template_folder="templates") #creating the application


habits_folder_path = "data/habits"
print_text = ""

habits = [["habit1",[1,2]],["habit2",[0,1]]]
'''{
	"habit1":{"date_1":n,"date_2":n,"date_3":n}],
	"habit2":{"date_1":n,"date_2":n,"date_3":n}]
	}
'''


@app.route("/")
def index():
	# open habits_folder_path and
	habits = []
	habits_files = listdir(habits_folder_path)
	for i in habits_files:
		pass
		# open file
		# add "habit_name":{} to habits
		# get first 15 elements or any elements if there are less
			# add "date":n to "habit_name:{}"
	return render_template("index.html", habits=habits, habits_files=habits_files, print_text=print_text)


@app.route("/add_habit", methods=["POST"])
def add_habit():
	return redirect(url_for("index"))

@app.route("/habits_submit", methods=["POST"])
def habits_submit():
	return redirect(url_for("index"))



if __name__ == "__main__":
	app.run(debug=True)	