# import Flask class from flask 
from flask import Flask, render_template, redirect, url_for, request, session, flash

# create app obj
app = Flask(__name__)

app.secret_key = "my little house in my mind"

# decorating link of url
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

# route for handling the lgin page logic
@app.route('/login', methods =['GET', 'POST'])
def login():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('Your were just logged in!')
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Your were just logged in!')
	return redirect(url_for('welcome'))

# starts the server with the run()
if __name__ == '__main__':
	app.run(debug = True)