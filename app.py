from flask import Flask,redirect, url_for, request, render_template  

app = Flask(__name__)

@app.route("/signin") 
def signin():
    return render_template("signin.html")

@app.route("/signup") 
def signup():
    return render_template("signup.html")

@app.route("/") 
def user():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)