# 🐾 Pet Care Manager (Flask + SQLite)

A simple **Flask web application** to manage pets, store their details in an **SQLite database**, and provide REST API endpoints for search and deletion.  

---

## 📂 Project Structure

```
├── app.py # 🐍 Main Flask application
├── database.py # 🗄️ Database helper functions
├── init_db.py # 🛠️ Script to initialize the database
├── static/ # 🎨 (Optional) static assets (CSS, JS, images)
├── templates/ # 🖼️ HTML templates (Jinja2)
└── README.md # 📖 Project documentation
```

---

## 🎮 Features

- 🐶 **Add Pet** → Store name, breed, age, gender, vaccination status  
- 📋 **View Pets** → Fetch all pets from the database  
- 🔍 **Search Pets** → Search by name via `/api/search?name=<query>`  
- ❌ **Delete Pet** → Delete pet records by ID  
- 🌐 **REST API endpoints** for integration with other applications  

---

## 🛠 Requirements

- **Python 3.8+**
- Flask  
- SQLite3 (bundled with Python)  

Install dependencies:  

```
pip install flask
```

---

## ▶️ Running the Application

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/pet-care-manager.git
   cd pet-care-manager
   ```
2. **Initialize the database**
   ```
   python init_db.py
   ```
3. **Start the Flask app**
   ```
   python app.py
   ```
4. **Open in browser:**
👉 http://127.0.0.1:5000

---

## 📡 API Endpoints

| Endpoint                   | Method | Description                  |
|-----------------------------|--------|------------------------------|
| `/`                        | GET    | Render homepage (index.html) |
| `/add-pet`                 | POST   | Add a new pet                |
| `/api/pets`                | GET    | Get all pets in JSON format  |
| `/api/search?name=<query>` | GET    | Search pets by name          |
| `/api/delete/<pet_id>`     | DELETE | Delete pet by ID             |

---

## 🖥️ Example JSON Response

### GET `/api/pets`

```json
[
  {
    "id": 1,
    "name": "Buddy",
    "breed": "Golden Retriever",
    "age": 3,
    "gender": "Male",
    "vaccination_status": "Up to date"
  }
]
```

---

## 📌 Roadmap

- ✅ Add CRUD operations (Create, Read, Update, Delete)  
- ✅ Provide REST API support  
- ⏳ Add authentication (user login system)  
- ⏳ Improve UI with Bootstrap / Tailwind CSS  
- ⏳ Deploy on Heroku / Render  
