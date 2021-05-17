from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1><align=center><color=orange>Welcome Home !</h1></align></color>"

@app.route("/users/<name>/")
def goto_user(name):
    return f"<h1><align=center><color=orange>Welcome {name}</h1></align></color>"


if __name__ == "__main__":
    app.run(debug=True)