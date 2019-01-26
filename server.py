from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def mypage():
    return render_template('index.html')

@app.route('/resume')
def resumepage():
	return render_template('resume.html')  

@app.route('/newresume')
def newresumepage():
	return render_template('newresume.html')
