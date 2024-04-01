from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network.db'
db = SQLAlchemy(app)


class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.String(5), nullable=False)
    drink = db.Column(db.Text())
    descr = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'post id: {self.id}, its drink: {self.drink}, price: {self.price}, descr: {self.descr} date: {self.date}'


class Num(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    def __repr__(self):
        return f'order id: {self.id}'


@app.route('/')
def index():
    # post01 = Order(price='30.00₴', drink='Macchiato', descr='Milk foam; Espresso')
    # db.session.add(post01)
    # db.session.commit()
    # post02 = Order(price='36.00₴', drink='Latte with Cream', descr='Ice Cream; Milk Foam; Steamed Milk; Espresso')
    # db.session.add(post02)
    # db.session.commit()
    # post03 = Order(price='37.00₴', drink='Irish Coffee', descr='Whipped Cream; Whiskey; Espresso')
    # db.session.add(post03)
    # db.session.commit()
    posts = Order.query.all()
    # return f'{posts}'
    # return redirect(url_for('sign_up'))
    return render_template('posts.html', posts=posts)


@app.route('/order', methods=['GET'])
def index1():
    selected_drink = request.args.get('drink')
    if selected_drink == 'Macchiato':
        drink = Order.query.get(1)
        return render_template('orderdrink.html', drink=drink)
    elif selected_drink == 'Latte with Cream':
        drink = Order.query.get(2)
        return render_template('orderdrink.html', drink=drink)
    elif selected_drink == 'Irish Coffee':
        drink = Order.query.get(3)
        return render_template('orderdrink.html', drink=drink)
    else:
        return render_template('index.html')


@app.route('/ordered/', methods=['GET'])
def index2():
    ide = request.args.get('id')
    order = Num(id=ide)
    db.session.add(order)
    db.session.commit()
    order_number = Num.query.all()
    return render_template('ordered.html', order_number=order_number)


with app.app_context():
    db.create_all()


app.run(debug=True)