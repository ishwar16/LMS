from logging import log
from flask import Flask, redirect, url_for, request, Response, render_template, session
import secrets  
import hashlib
import requests

from flask.helpers import make_response

app = Flask(__name__)

#Default User (for now)
#User Name: Yo123
#User Email: yo123@mail.com
#User Entered Pass: Yok@1234
#User Pass Hash: b'\xce\xc8\xc6\x9d\xcf|H\xa0C\x07\xfd}\x9c\xf6\nvv\x84SQ\t$_\r\xcc\xdd\x04~\xb7\x88\xf67!\x90\xae}3cz\xf6~\xaf\xf5\xc6'
#User Identifier(just a 5 digit random number): 83732

class LoginCheck:
    error = list()
    loginPass = 0
    def __init__(self, emailID, pas, uType):
        self.emailID = self.isEmpty(emailID,"EmailID was not given.")
        self.password = self.isEmpty(pas,"Password was not given.")
        self.uType = self.isEmpty(uType,"User Type was not given.")

    def isEmpty(self, val, errorMessage):
        if val is None:
            self.error.append(errorMessage)
        return val

    def __isPassRight(self, password):
        SaltFromPassword = password[:12]
        KeyFromPassword = password[12:]
        newKey = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), SaltFromPassword, 100000)
        if (KeyFromPassword == newKey):
            return True
        self.error.append("Given Password is wrong.")
        return False
    
    def check(self):
        if(len(self.error) == 0):
            # query = "SELECT Password FROM "+self.uType+" WHERE 'Email Address' = "+self.emailID
            emailID = "yo123@mail.com"
            if self.emailID == emailID:
                password = b'\xf5+\xdf\xebkX\x8f\xb7|\xed\x85\xd4\xe8H\xac\x12/I\xc7~\x9b9]F\xba\xec\xf5\xd5\x98\xa8\xb5 ^*<)!"\xb4\xe6hIms'
                if self.__isPassRight(password):
                    self.loginPass = 1
                    return True
            else:
                self.error.append("EmailID does not exist.")
        return False
    
    def getDetails(self,rem=None):
        if(self.loginPass==1):
            # query = "SELECT Name,UserID,Password FROM "+self.uType+" WHERE 'Email Address' = "+self.emailID
            name = "Yo123"
            userid = "1234"
            password = b'\xf5+\xdf\xebkX\x8f\xb7|\xed\x85\xd4\xe8H\xac\x12/I\xc7~\x9b9]F\xba\xec\xf5\xd5\x98\xa8\xb5 ^*<)!"\xb4\xe6hIms'
            password = str(password[:12])
            if rem!=None:
                value = self.uType[0]+":" + self.setUserID(userid)+":" + password[:12]
                resp = make_response(render_template('signin.html'))
                resp.set_cookie('UserIdentifer',value)
            return userid,name
        return False
    
    def setUserID(self,userID):
        new = set()
        for i in range(0,len(userID)):
            new.add(chr(i+65)+userID[i])
        new = "".join(new)
        return new

    def getUserID(self,txt):
        txt = list(txt)
        new = [''] * int(len(txt)/2)
        for i in range(0,len(txt),2):
            new[ord(txt[i])-65] = txt[i+1]
        new = "".join(new)
        return new

def checkCookie():
    cookie = request.cookies.get('UserIdentifer')
    if cookie is not None:
        uType,userID,passwordHash = cookie.split(':')
        userID = LoginCheck.getUserID(userID)
        # query = "SELECT Password FROM "+uType+" WHERE 'UserID' = "+userID
        password = b'\xce\xc8\xc6\x9d\xcf|H\xa0C\x07\xfd}\x9c\xf6\nvv\x84SQ\t$_\r\xcc\xdd\x04~\xb7\x88\xf67!\x90\xae}3cz\xf6~\xaf\xf5\xc6'    
        if(passwordHash == str(password[:12])):
            # query = "SELECT Name FROM "+uType+" WHERE 'UserID' = "+userID
            name = "Yo123"
            return [userID,name,uType]
    return False

@app.route("/signin", methods = ['POST','GET']) 
def signin():
    v = 12
    if(not 'User' in session):
        cookieResult = checkCookie()
        if cookieResult is False:
            if request.method == 'POST':
                email = request.form.get('EmailID')
                pas = request.form.get('Password')
                rem = request.form.get('RememberMe')
                userType = request.form.get('userType')
                login = LoginCheck(email,pas,userType)
                if (login.check() == True):
                    userID,name = login.getDetails(rem)
                    session['UserID'] = userID
                    session['User'] = name
                    session['UserType'] = userType
                    return redirect("/")
                else:
                    return render_template("signin.html",result = login.error,email = login.emailID, password = login.password, rem = rem)
            return render_template('signin.html')
        else:
            session['UserID'] = cookieResult[0]
            session['User'] = cookieResult[0]
            session['UserType'] = cookieResult[0]
    return redirect("/")


@app.route("/signup") 
def signup():
    return render_template("signup.html")

@app.route("/") 
def user():
    if 'User' in session:
        return render_template("user.html",user=session['User'])
    return redirect('/signin')


app.config['SECRET_KEY']  = secrets.token_hex(16)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)