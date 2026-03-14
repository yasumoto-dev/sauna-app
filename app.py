from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    saunas = [
        {"name": "お風呂の王様 和光店", "area": "埼玉"},
        {"name": "かるまる池袋", "area": "東京"},
        {"name": "スパメッツァおおたか", "area": "千葉"},
    ]
    return render_template("index.html",saunas=saunas)

if __name__ == "__main__":
    app.run(debug=True)    