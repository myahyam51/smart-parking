from flask import Flask, render_template
from database import create_tables, insert_default_parking

app = Flask(__name__)

app.config["SECRET_KEY"] = "smartparking_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    create_tables()
    insert_default_parking()
    app.run(debug=True)