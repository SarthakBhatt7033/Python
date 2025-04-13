from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            result = eval(expression)
        except:
            result = "Error"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
