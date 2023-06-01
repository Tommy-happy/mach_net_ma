from flask import Flask, render_template, request, redirect, url_for, session, json
import sqlite3

app = Flask(__name__)
app.secret_key = "b22VD7bKVsEa"

# login register --------------------------------------------------
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login_action",methods=["POST"])
def login_action():
    user_name = request.form.get("user")
    password = request.form.get("pwd")
    print(user_name,password)
    return check_user_exist(user_name,password)

@app.route("/<msg>")
def return_login(msg):
    return render_template("login.html",msg=msg)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register/<msg>")
def return_register(msg):
    return render_template("register.html",msg=msg)

@app.route("/register_action",methods=["POST"])
def register_action():
    user_name = request.form.get("user")
    password = request.form.get("pwd")
    return add_user(user_name, password)

@app.route("/main")
def main_page():
    return render_template("main.html")

@app.route("/score")
def score():
    all_user = []    
    all_user = get_first_five_user()
    return render_template("score_page.html",all=all_user[:5], me=all_user[-1])

# game------------------------------------------------------
@app.route("/zombie_first")
def zombie_first():
    return render_template("./game/zombie/zombieFirst.html")

@app.route("/zombie_main")
def zombie_main():
    return render_template("./game/zombie/zombie3c.html")

@app.route("/renew_zombie_score",methods=["POST"])
def renew_zombie_score():
    # score = int(request.get_data().decode("utf-8"))
    score = int(request.data.decode("utf-8"))
    old_score = get_user_score("zombie")
    if(score>old_score):
        renew_user_score("zombie", score)
        return "new record"
    else:
        return "ok"
    
@app.route("/g2048_main")
def g2048():
    return render_template("./game/2048/main.html")

@app.route("/renew_2048_score",methods=["POST"])
def renew_2048_score():
    # score = int(request.get_data().decode("utf-8"))
    score = int(request.data.decode("utf-8"))
    old_score = get_user_score("g2048")
    if(score>old_score):
        renew_user_score("g2048", score)
        return "new record"
    else:
        return "ok"

@app.route("/boom_main")
def boom():
    # return render_template("./game/boom/boom.html")
    return render_template("./game/boom/temp.html")

@app.route("/renew_boom_score",methods=["POST"])
def renew_boom_score():
    # score = int(request.get_data().decode("utf-8"))
    score = int(request.data.decode("utf-8"))
    old_score = get_user_score("boom")
    if(score<old_score or old_score==0):
        renew_user_score("boom", score)
        return "new record"
    else:
        return "ok"


def add_user(user, password):
    con = sqlite3.connect("project.db")
    c = con.cursor()
    if user=='' or password=='':
        return redirect(url_for("return_register",msg="user name or password should be inputted"))
    c.execute(f"select * from users where user_name = '{user}'")
    if c.fetchone():
        return redirect(url_for("return_register",msg="the user is already existed!!"))
    else:
        c.execute(f"insert into users (user_name,user_password) values ('{user}','{password}')")
        con.commit()
        c.execute(f"select id from users where user_name = '{user}' ")
        id = c.fetchone()[0]
        print(id)
        c.execute(f"insert into score (user_id,g2048_score,boom_score,zombie_score) values ({id},0,1000,0)")
        con.commit()
        return redirect(url_for("login"))

def check_user_exist(user,password):
    con = sqlite3.connect("project.db")
    c = con.cursor()
    if user=="" or password=="":
        print(user, password)
        return redirect(url_for("return_login",msg="user name or password can not be empty"))
    c.execute(f"select user_password from users where user_name = '{user}'")
    pwd = c.fetchone()
    if pwd:
        if(pwd[0] == password):
            # print(password)
            # print(pwd)
            # session["user"] = user
            session["user_id"] = get_user_id(user)
            return redirect(url_for("main_page"))
        else:
            return redirect(url_for("return_login",msg="wrong password!!"))    
    else:
        return redirect(url_for("return_login",msg="the user is not found!!"))

def get_user_score(game):
    con = sqlite3.connect("project.db")
    c = con.cursor()
    c.execute(f"select {game}_score from score where user_id={session['user_id']}")
    return int(c.fetchone()[0])

def get_user_id(user):
    con = sqlite3.connect("project.db")
    c = con.cursor()
    c.execute(f"select id from users where user_name='{user}'")
    return c.fetchone()[0]

def renew_user_score(game, score):
    con = sqlite3.connect("project.db")
    c = con.cursor()
    c.execute(f"update score set {game}_score={score} where user_id={session['user_id']}")
    con.commit()
    # return 0

def get_first_five_user():
    session_id = session["user_id"]
    con = sqlite3.connect("project.db")
    c = con.cursor()
    all = []
    row = []
    row2=[]
    c.execute("select user_id from score order by g2048_score DESC")
    row = c.fetchall()[:5]
    # print(all)
    # print(c.fetchall()[:5])
    c.execute(f"select user_name from users where id={row[0][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[1][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[2][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[3][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[4][0]}")
    row2.append(c.fetchone())
    all.append(row2)

    row = []
    row2=[]
    c.execute("select user_id from score order by boom_score")
    row = c.fetchall()[:5]
    # print(all)
    # print(c.fetchall()[:5])
    c.execute(f"select user_name from users where id={row[0][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[1][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[2][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[3][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[4][0]}")
    row2.append(c.fetchone())
    all.append(row2)

    row = []
    row2=[]
    c.execute("select user_id from score order by zombie_score DESC")
    row = c.fetchall()[:5]
    # print(all)
    # print(c.fetchall()[:5])
    c.execute(f"select user_name from users where id={row[0][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[1][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[2][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[3][0]}")
    row2.append(c.fetchone())
    c.execute(f"select user_name from users where id={row[4][0]}")
    row2.append(c.fetchone())
    all.append(row2)

    row = []
    row2=[]
    c.execute(f"select g2048_score,boom_score,zombie_score from score where user_id={session_id}")
    row = c.fetchone()
    print(row)    
    print("-------=-=-=-=-=-")
    all.append([row])



    return all



if __name__ == "__main__":
    app.run(debug=True)