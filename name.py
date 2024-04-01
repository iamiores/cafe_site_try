from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)



@app.route('/')
def index():
    return redirect(url_for('sign_up'))


@app.route('/sign_up')
def sign_up():
    return render_template('index.html')


@app.route('/1')
def index1():
    return redirect(url_for('log_in'))


@app.route('/log_in')
def log_in():
    return render_template('index3.html')


@app.route('/2')
def index2():
    return redirect(url_for('main'))


@app.route('/main')
def main():
    return render_template('index2.html')


app.run(debug=True)