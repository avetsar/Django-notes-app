from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(os.path.join(os.getcwd(), '..', 'db.sqlite3'))
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/notes', methods=['GET'])
def get_notes():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes_note').fetchall()
    conn.close()
    notes_list = [{"id": note["id"], "title": note["title"], "content": note["content"]} for note in notes]
    return jsonify(notes_list)


if __name__ == "__main__":
    app.run(port=5000)
