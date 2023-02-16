from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/score/<int:score>")
def main(score):
    return render_template("index.html", score = score )

@app.route("/result/")
def getresult():
    dict = {'fiizk': 60, 'matematik': 70, 'python': 100}
    return render_template("result.html", result = dict)

@app.route("/login")
def login():
    return render_template("form.html")


@app.route("/sonuclar", methods = ['POST', 'GET','UPDATE'])
def sonuclar():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)



if __name__ == "__main__":
    app.run()
