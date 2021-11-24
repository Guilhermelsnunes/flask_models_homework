from flask import render_template
from app import app
from models.customer import customers

@app.route("/orders")
def index():
    return render_template("index.html", title="Toy Store", all_customers=customers )


@app.route("/orders/<index>")
def order(index):
    index_number=int(index)
    order=customers[index_number]
    return render_template("order.html", title="home", customer=order)

