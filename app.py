
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to DevOps Lab</h1>
    <p>Docker, Jenkins and Selenium</p>
    <a href="/add?a=10&b=20">Addition</a>
    """

@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"<h2 id='result'>Result: {a+b}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
