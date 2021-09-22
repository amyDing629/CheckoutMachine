from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/index2')
def add_item():
   return render_template('index2.html')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)