from flask import Flask

app = Flask(__name__)

@app.route("/bot", methods=['"POST'])
def bot():
    pass


if __name__ == "__main__":
    app.run()