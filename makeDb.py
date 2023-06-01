import sqlite3

# connection = sqlite3.connect("project.db")
# cu = connection.cursor()

# cu.execute("DROP TABLE user")

# cu.execute("""create table users(
#     id INTEGER primary key,
#     user_name TEXT,
#     user_password TEXT
# )""")

# cu.execute("""create table g2048(
#     user_id INTEGER,
#     score INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# )""")

# cu.execute("""create table snake(
#     user_id INTEGER,
#     score INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# )""")

# cu.execute("""create table zombie(
#     user_id INTEGER,
#     score INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# )""")

# cu.execute("""create table score(
#     user_id INTEGER,
#     g2048_score INTEGER,
#     snake_score INTEGER,
#     zombie_score INTEGER,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# )""")
users = [
    ("Tommy", "password"),
    ("Sammy", "passw"),
    ("Jimmy", "pass2word"),
    ("Tom", "paswgw"),
    ("John", "apppple")
]
# cu.execute("delete from users")
# cu.executemany(f"insert into users (user_name,user_password) values (?,?)", users)
# cu.execute("delete from users where user_name='Tommy'")

# cu.execute("insert into snake values (1, 99)")
# cu.execute("insert into g2048 values (1, 98)")
# cu.execute("insert into zombie values (1, 97)")

# cu.execute(f"""insert into score values (
#     1,
#     {cu.execute("select score from g2048 where user_id=1").fetchone()[0]},
#     {cu.execute("select score from snake where user_id=1").fetchone()[0]},
#     {cu.execute("select score from zombie where user_id=1").fetchone()[0]}
# )""")
# cu.execute(f"insert into users (user_name,user_password) values ('Ian','ianian123')")


# connection.commit()
# cu.close()
# connection.close()

def get_first_five_user():
    session = 8
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
    c.execute("select user_id from score order by boom_score DESC")
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
    c.execute(f"select g2048_score,boom_score,zombie_score from score where user_id={session}")
    row = c.fetchone()
    print(row)    
    print("-------=-=-=-=-=-")
    all.append([row])



    return all


print(get_first_five_user())