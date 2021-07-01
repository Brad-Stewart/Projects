from flask import Flask
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template("index.html", num = 3, tempColor = "blue")

@app.route("/play/<int:num_box>")
def level2(num_box):
    print(num_box)
    return render_template("index.html", num = num_box)

@app.route("/play/<int:num_box>/<color>")
def leve3(num_box, color):
    return render_template("index.html", num = num_box, tempColor = color)

if__name__="__main__":
app.run(debug = True)