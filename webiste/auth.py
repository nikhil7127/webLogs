from flask import Blueprint,render_template,request,flash

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<h1>logout Page</h1>"

@auth.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        signUpdata = request.form
        first_name = signUpdata.get("first-name")
        last_name = signUpdata.get("last-name")
        email = signUpdata.get("email")
        password= signUpdata.get("password")
        confirm = signUpdata.get("confirm")

        if(len(first_name)<5):
            flash("Enter valid first name",category="error")
        elif(len(last_name)<5):
            flash("Enter valid last name",category="error")
        elif(len(email)<5 and "@" not in email):
            flash("Enter valid email",category="error")
        elif(password!=confirm):
            flash("Both passwords must be same",category="error")
        else:
            flash("Account created!",category="success")
    


    return render_template("signup.html")