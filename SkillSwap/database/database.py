import sqlite3
from datetime import datetime
from theme import *

# =====================================
# CREATE DATABASE
# =====================================
def create_database():

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            skill TEXT,
            learn_skill TEXT
        )
    """)

    # Add About column if it doesn't exist
    try:
        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN about TEXT
        """)
    except:
        pass

    # Requests Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER,
            receiver_name TEXT,
            status TEXT DEFAULT 'Pending',
            request_date TEXT
        )
    """)

    # Add request_date column if it doesn't exist
    try:
        cursor.execute("""
            ALTER TABLE requests
            ADD COLUMN request_date TEXT
        """)
    except:
        pass

    connection.commit()
    connection.close()


# =====================================
# REGISTER USER
# =====================================
def register_user(name, email, password, skill, learn_skill):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users(
            name,
            email,
            password,
            skill,
            learn_skill,
            about
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, password, skill, learn_skill, ""))

    connection.commit()
    connection.close()


# =====================================
# LOGIN USER
# =====================================
def login_user(email, password):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE email=? AND password=?
    """, (email, password))

    user = cursor.fetchone()

    connection.close()

    return user


# =====================================
# GET ALL USERS
# =====================================
def get_all_users(current_user):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            name,
            skill,
            learn_skill
        FROM users
        WHERE name != ?
    """, (current_user,))

    users = cursor.fetchall()

    connection.close()

    return users


# =====================================
# SEARCH USERS
# =====================================
def search_users(search_text):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    search = "%" + search_text.lower() + "%"

    cursor.execute("""
        SELECT name, skill, learn_skill
        FROM users
        WHERE LOWER(name) LIKE ?
           OR LOWER(skill) LIKE ?
           OR LOWER(learn_skill) LIKE ?
    """, (search, search, search))

    users = cursor.fetchall()

    connection.close()

    return users


# =====================================
# UPDATE USER
# =====================================
def update_user(user_id, name, skill, learn_skill, about):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE users
    SET
        name=?,
        skill=?,
        learn_skill=?,
        about=?
    WHERE id=?
""", (
    name,
    skill,
    learn_skill,
    about,
    user_id
))

    connection.commit()
    connection.close()


# =====================================
# SEND REQUEST
# =====================================
def send_request(sender_id, receiver_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    print("Sender ID:", sender_id)
    print("Receiver:", receiver_name)

    cursor.execute("""
        SELECT *
        FROM requests
        WHERE sender_id=?
        AND receiver_name=?
        AND status='Pending'
    """, (sender_id, receiver_name))

    existing = cursor.fetchone()

    print("Existing Request:", existing)

    if existing:
        connection.close()
        return False

    current_time = datetime.now().strftime("%d %b %Y, %I:%M %p")

    cursor.execute("""
        INSERT INTO requests(
            sender_id,
            receiver_name,
            request_date
        )
        VALUES(?, ?, ?)
    """, (
        sender_id,
        receiver_name,
        current_time
    ))

    connection.commit()
    connection.close()

    return True

# =====================================
# GET REQUEST STATUS
# =====================================
def get_request_status(sender_id, receiver_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT status
        FROM requests
        WHERE sender_id=?
        AND receiver_name=?
    """, (sender_id, receiver_name))

    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]

    return None

# =====================================
# GET REQUESTS
# =====================================
def get_requests(receiver_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            requests.id,
            users.name,
            users.skill,
            users.learn_skill,
            requests.status,
            requests.request_date
        FROM requests
        JOIN users
            ON requests.sender_id = users.id
        WHERE requests.receiver_name=?
    """, (receiver_name,))

    requests = cursor.fetchall()

    connection.close()

    return requests


# =====================================
# ACCEPT REQUEST
# =====================================
def accept_request(request_id):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE requests
        SET status='Accepted'
        WHERE id=?
    """, (request_id,))

    connection.commit()
    connection.close()


# =====================================
# REJECT REQUEST
# =====================================
def reject_request(request_id):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE requests
        SET status='Rejected'
        WHERE id=?
    """, (request_id,))

    connection.commit()
    connection.close()

    # =====================================
# COUNT PENDING REQUESTS
# =====================================
def get_pending_request_count(receiver_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM requests
        WHERE receiver_name=?
        AND status='Pending'
    """, (receiver_name,))

    count = cursor.fetchone()[0]

    connection.close()

    return count

# =====================================
# GET USER ID
# =====================================
def get_user_id(user_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE name=?
    """, (user_name,))

    user = cursor.fetchone()

    connection.close()

    if user:
        return user[0]

    return None
# =====================================
# GET HISTORY
# =====================================
def get_history(user_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    # Get logged-in user's ID
    cursor.execute("""
        SELECT id
        FROM users
        WHERE name=?
    """, (user_name,))

    user = cursor.fetchone()

    if user:
        user_id = user[0]
    else:
        connection.close()
        return [], []

    # ==========================
    # RECEIVED REQUESTS
    # ==========================
    cursor.execute("""
        SELECT
            users.name,
            users.skill,
            users.learn_skill,
            requests.status,
            requests.request_date
        FROM requests
        JOIN users
            ON requests.sender_id = users.id
        WHERE requests.receiver_name=?
    """, (user_name,))

    received = cursor.fetchall()

    # ==========================
    # SENT REQUESTS
    # ==========================
    cursor.execute("""
        SELECT
            requests.receiver_name,
            users.skill,
            users.learn_skill,
            requests.status,
            requests.request_date
        FROM requests
        JOIN users
            ON requests.receiver_name = users.name
        WHERE requests.sender_id=?
    """, (user_id,))

    sent = cursor.fetchall()

    connection.close()

    return received, sent

# =====================================
# GET ABOUT
# =====================================
def get_about(user_name):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT about
        FROM users
        WHERE name=?
    """, (user_name,))

    result = cursor.fetchone()
    print("Getting about for:", user_name)
    print("Result:", result)

    connection.close()

    if result and result[0]:
        return result[0]

    return "This user hasn't added an introduction yet."

# =====================================
# DASHBOARD STATISTICS
# =====================================
def get_dashboard_stats(user):

    connection = sqlite3.connect("skillswap.db")
    cursor = connection.cursor()

    user_id = user[0]
    user_name = user[1]

    # Total users
    cursor.execute("""
        SELECT COUNT(*)
        FROM users
    """)
    total_users = cursor.fetchone()[0]

    # Pending Requests
    cursor.execute("""
        SELECT COUNT(*)
        FROM requests
        WHERE receiver_name=?
        AND status='Pending'
    """, (user_name,))
    pending = cursor.fetchone()[0]

    # Accepted Swaps
    cursor.execute("""
        SELECT COUNT(*)
        FROM requests
        WHERE
        (sender_id=? OR receiver_name=?)
        AND status='Accepted'
    """, (user_id, user_name))
    accepted = cursor.fetchone()[0]

    # Total Requests
    cursor.execute("""
        SELECT COUNT(*)
        FROM requests
        WHERE
        sender_id=? OR receiver_name=?
    """, (user_id, user_name))
    total_history = cursor.fetchone()[0]

    connection.close()

    return (
        total_users,
        pending,
        accepted,
        total_history
    )
