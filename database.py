import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('pet_care.db')
cursor = conn.cursor()

# Function to add a new pet
def add_pet(name, breed, age, gender, vaccination_status):
    cursor.execute('''
    INSERT INTO Pet (name, breed, age, gender, vaccination_status)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, breed, age, gender, vaccination_status))
    conn.commit()

# Function to view all pets
def view_pets():
    cursor.execute('SELECT * FROM Pet')
    pets = cursor.fetchall()
    for pet in pets:
        print(f"ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}, Age: {pet[3]}, Gender: {pet[4]}, Vaccination Status: {pet[5]}")

# Function to add a health record
def add_health_record(pet_id, date, treatment, vet_name, notes):
    cursor.execute('''
    INSERT INTO Health_Record (pet_id, date, treatment, vet_name, notes)
    VALUES (?, ?, ?, ?, ?)
    ''', (pet_id, date, treatment, vet_name, notes))
    conn.commit()

# Function to view health records for a specific pet
def view_health_records(pet_id):
    cursor.execute('SELECT * FROM Health_Record WHERE pet_id = ?', (pet_id,))
    records = cursor.fetchall()
    for record in records:
        print(f"Record ID: {record[0]}, Date: {record[2]}, Treatment: {record[3]}, Vet: {record[4]}, Notes: {record[5]}")

# Example usage
if __name__ == "__main__":
    # Add a new pet
    add_pet("Max", "Golden Retriever", 5, "Male", "Up-to-date")
    
    # View pets
    print("Pets in the system:")
    view_pets()
    
    # Add health record for the pet (assume Max's pet_id is 1)
    add_health_record(1, "2023-05-01", "Vaccination", "Dr. Smith", "Routine vaccination")
    
    # View health records for pet with ID 1
    print("\nHealth Records for Max:")
    view_health_records(1)

# Close connection
conn.close()
