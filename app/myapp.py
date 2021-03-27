from flask import Flask
app = Flask(__name__)
@app.route("/")
def test():
    return "<h1>Netprog.io server is working!</h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)