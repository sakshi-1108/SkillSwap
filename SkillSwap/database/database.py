import sqlite3

def create_database():
    ...
    # Your existing code


def register_user(name, email, password, skill, learn_skill):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users(name, email, password, skill, learn_skill)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, password, skill, learn_skill))

    connection.commit()
    connection.close()


def login_user(email, password):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print(users)

    cursor.execute("""
        SELECT * FROM users
        WHERE email=? AND password=?
    """, (email, password))

    user = cursor.fetchone()

    connection.close()

    return user



def get_all_users():

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, skill, learn_skill
        FROM users
    """)

    users = cursor.fetchall()
    print("All Users:", users)

    connection.close()

    return users
def search_users(search_text):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, skill, learn_skill
        FROM users
        WHERE
            LOWER(name) LIKE ?
            OR LOWER(skill) LIKE ?
            OR LOWER(learn_skill) LIKE ?
    """, (
        "%" + search_text.lower() + "%",
        "%" + search_text.lower() + "%",
        "%" + search_text.lower() + "%"
    ))

    users = cursor.fetchall()

    connection.close()

    return users
def update_user(user_id, name, skill, learn_skill):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET name=?,
            skill=?,
            learn_skill=?
        WHERE id=?
    """, (name, skill, learn_skill, user_id))

    connection.commit()
    connection.close()