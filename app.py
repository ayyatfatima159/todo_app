from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)
DB = 'todo.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM todos')
    todos = c.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
