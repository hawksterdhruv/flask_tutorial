from flask import Flask, render_template, request

app = Flask(__name__)


todo = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        todo.append(dict(request.form))
    return render_template("home.html", data=todo)


if __name__ == "__main__":
    app.run(debug=True)
