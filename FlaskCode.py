from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def website():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)


def posts():
    if request.method == 'POST':
        tag = request.form['tag']  # The get the data from the form



