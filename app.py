from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

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

    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO pets (name, breed, age, gender, vaccination_status) VALUES (?, ?, ?, ?, ?)",
              (name, breed, age, gender, vaccination_status))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/api/pets')
def api_pets():
    conn = connect_db()
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
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM pets WHERE name LIKE ?", (f'%{name_query}%',))
    rows = c.fetchall()
    conn.close()
    pets = [dict(row) for row in rows]
    return jsonify(pets)

@app.route('/api/delete/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Pet deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
