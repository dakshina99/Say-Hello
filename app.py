from flask import Flask, render_template, request, redirect
import random

from flask.helpers import url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    global a
    with open("Index.txt") as f:
        a = list(map(lambda x: x.strip("\n"), f.readlines()))

    if request.form.get('randomGet'):
        return redirect(url_for('index'))

    return render_template("main.html")


@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.form.get("end"):
        return redirect(url_for('home'))

    if request.form.get("main"):
        return redirect(url_for('home'))

    if request.form.get("submit"):

        if len(a) > 1:
            index = random.choice(a)
            a.remove(index)
            return render_template('random.html', indexNo=index)

        elif len(a) == 1:
            index = random.choice(a)
            a.remove(index)
            return render_template("end.html", indexNo=index)

        else:
            return redirect(url_for('home'))

    index = random.choice(a)
    a.remove(index)
    return render_template('random.html', indexNo=index)


if __name__ == "__main__":
    app.run(debug=True)
