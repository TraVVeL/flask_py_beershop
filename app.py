from flask import Flask, render_template, g
import sqlite3
import os
from ADataBase import ADataBase

# configuration
DATABASE = '/tmp/database.db'
DEBUG = True
SECRET_KEY = 'lj465l45nlhkl64l5k6l;jl;bf0c87nb'

#
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))


# connect to database
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Helper function for creating database tables"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """DB connection if not already established"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """Close the connection to the database if it was established"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()
    dbase = ADataBase(db)
    return render_template("index.html", products=dbase.get_products())


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/blog_single")
def blog_single():
    return render_template("blog-single-sidebar.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
