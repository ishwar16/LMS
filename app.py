from flask import Flask,redirect, url_for, request, render_template  

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("login.html")

@app.route("/homepage") 
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods =["POST", "GET"]) 
def login():
    username = request.args.get("email")
    pwd = request.args.get("pswd")
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.run(debug=True)