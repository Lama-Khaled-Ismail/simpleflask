from flask import Flask, redirect, render_template ,request, url_for ,session

app = Flask(__name__,static_url_path='/static')
app.secret_key="ToolsProject"


@app.route("/")
def home():
    return "<h1>Hello! this is the main page<h1>"

@app.route("/SignIn",methods=["POST","GET"])
def SignIn():
    if request.method == "POST":
        email=request.form["email"]
        session["email"]=email
        return redirect(url_for("user",mail=email))
    else:
        return render_template("SignIn.html")
    
@app.route("/user")
def user():
    if "email" in session:
        user = session["email"]
        return f"<h1> HELLO! {user}</h1>"
    else:
        return redirect(url_for("SignIn"))

if __name__ =="__main__":
    app.run(debug=True)

