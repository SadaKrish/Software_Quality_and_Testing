from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "CI/CD with GCP is working!"

@app.route("/add")
def add():
    return str(2+2)
if __name__=="__main__":
    app.run(debug=True)