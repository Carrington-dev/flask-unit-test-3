In Flask, you can use **Flask-Migrate** (which is built on top of **Alembic**) to handle database migrations. This allows you to modify your database schema without losing existing data.

---

## **Step 1: Install Dependencies**
If you haven’t installed Flask-Migrate and Flask-SQLAlchemy yet, install them using:
```bash
pip install Flask-Migrate Flask-SQLAlchemy
```

---

## **Step 2: Set Up Flask App with SQLAlchemy & Migrate**
Modify your **Flask app** to integrate Flask-Migrate.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the database (Change this to your actual DB URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Example Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## **Step 3: Initialize Flask-Migrate**
Run the following commands in your terminal:

1. **Initialize migrations folder** (Creates a `migrations/` directory)
   ```bash
   flask db init
   ```

2. **Generate a migration script** (Detects changes in models)
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply the migration to the database**
   ```bash
   flask db upgrade
   ```

---

## **Step 4: Updating the Database Schema**
If you **modify your model**, repeat **Step 3**:
1. Edit your **models** (e.g., add a new column)
   ```python
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)
       age = db.Column(db.Integer)  # New column added
   ```
2. Run:
   ```bash
   flask db migrate -m "Added age column"
   flask db upgrade
   ```

---

## **Step 5: Rolling Back a Migration**
If needed, you can **undo** the last migration:
```bash
flask db downgrade
```
Or, check the history of migrations:
```bash
flask db history
```

---

💡 **Flask-Migrate Benefits**
---
✔️ Handles database changes safely  
✔️ Works with different database engines (PostgreSQL, MySQL, SQLite, etc.)  
✔️ No need to drop tables manually  

<!-- Would you like to integrate Flask-Migrate with **Docker** or another database like **PostgreSQL**? 🚀 -->