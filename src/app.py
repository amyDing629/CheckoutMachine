from flask import (
    Flask, 
    redirect, 
    url_for, 
    request, 
    render_template
)
from backend.checkout import CheckOut
app = Flask(__name__)
checkout = CheckOut()
@app.route('/additem', methods = ['POST', 'GET'])
def additem():
    if request.method == "POST":
        name = request.form.get("name")
        quantity = request.form.get("quantity")
        checkout.add_item_to_list(name, quantity)
        return redirect(url_for('index'))
    elif request.method == "GET":
        return render_template('additem.html')

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)