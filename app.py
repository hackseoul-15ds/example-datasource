from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b"exampledatasource"

users = {
    "hallazzang": {
        "name": "Hanjun Kim",
        "age": 33,
        "gender": "male",
        "salary": 3000,
        "role": "dev",
        "work_years": 8,
    },
    "yeonga": {
        "name": "Yeonga Jang",
        "age": 26,
        "gender": "female",
        "salary": 5000,
        "role": "pm",
        "work_years": 2,
    },
    "ryoochan": {
        "name": "Chan Ryoo",
        "age": 27,
        "gender": "male",
        "salary": 9000,
        "role": "design",
        "work_years": 3,
    },
}

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form["username"]
    if username not in users:
        return "Invalid login info", 400
    session["username"] = username
    return redirect(url_for("home"))

@app.get("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

@app.get("/me")
def me():
    username = session.get("username")
    if not username:
        return "You are not logged in", 401
    return users.get(username)
