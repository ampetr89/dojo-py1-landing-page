from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')


@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html')

@app.route('/success')
def success():
	return render_template('index.html', submitted=True)
	# this is a hack to redirect to the homepage but
	# passing a variable






app.run(debug=True)