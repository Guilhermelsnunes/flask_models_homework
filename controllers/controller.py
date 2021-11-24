from flask import render_template
from app import app
from models.customer import customers

@app.route("/orders")
def index():
    return render_template("index.html", title="Toy Store", all_customers=customers )

# @app.route("/orders/<index>")
#    def index(index):
#    return render_template("order.html", title="home", orders=orders, index=index_num)

