from flask import (
	Flask,
	render_template,
	redirect
)

app = Flask(__name__)

@app.route("/")
def home():
	pass

@app.route("/login")
def login():
	pass

@app.route("/send")
def homes():
	pass

if __name__  == "__main__":
	app.run(debug=True)