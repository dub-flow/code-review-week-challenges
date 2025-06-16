from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guestpass')")
    conn.commit()

def search_users(query):
    like_query = f"%{query}%"
    cursor.execute("SELECT * FROM users WHERE username LIKE ?", (like_query,))
    results = cursor.fetchall()
    return [{"id": row[0], "username": row[1]} for row in results]

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("user")
    results = search_users(query)
    return jsonify({"users": results})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
