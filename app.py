from flask import Flask,redirect, url_for, request, render_template  

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("login.html")

@app.route("/user") 
def user():
    return render_template("user.html")

@app.route("/login", methods =["POST", "GET"])
def login():
    username = request.args.get("email")
    pwd = request.args.get("pswd")
    return redirect(url_for('user'))

if __name__ == "__main__":
    app.run(debug=True)