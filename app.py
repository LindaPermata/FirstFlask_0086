
# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def order():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        cake_type = request.form.get("cake_type")
        quantity = request.form.get("quantity")
        message = f"Thank you, {name}! Your order of {quantity} {cake_type}(s) has been received."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
