from flask import Flask, render_template, request, redirect
import sqlite3
from flask import jsonify

app = Flask(__name__)

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('pet_care.db')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-pet', methods=['POST'])
def add_pet():
    name = request.form['name']
    breed = request.form['breed']
    age = request.form['age']
    gender = request.form['gender']
    vaccination_status = request.form['vaccination_status']

    conn = sqlite3.connect('pet_care.db')
    c = conn.cursor()
    c.execute("INSERT INTO pets (name, breed, age, gender, vaccination_status) VALUES (?, ?, ?, ?, ?)",
              (name, breed, age, gender, vaccination_status))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/api/pets')
def api_pets():
    conn = sqlite3.connect('pet_care.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM pets")
    rows = c.fetchall()
    conn.close()

    pets = [dict(row) for row in rows]
    return jsonify(pets)


@app.route('/api/search')
def search_pet():
    name_query = request.args.get('name', '').strip()
    conn = sqlite3.connect('pet_care.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM pets WHERE name LIKE ?", (f'%{name_query}%',))
    rows = c.fetchall()
    conn.close()
    pets = [dict(row) for row in rows]
    return jsonify(pets)


if __name__ == '__main__':
    app.run(debug=True)
