# 👶 Baby Feeding Tracker

This is a full-stack web application that helps caregivers track baby feeding sessions. The backend is built with **FastAPI**, and a frontend (in development) will use **Vue.js**.

## 🚀 Features

- ✅ Add a new feeding entry (with oz or ml)
- ✅ View all feeding entries
- ✅ Input validation (positive amounts, time not in the future)
- ✅ Sanitized notes
- 🛠️ Future: Delete and edit entries
- 🛠️ Future: Stats and summaries

## 🧪 Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite (currently)
- **Validation**: Pydantic v2
- **Frontend**: Vue.js (planned)

## 📦 Project Structure
<details> <summary>📁 <strong>Project Structure</strong></summary>
  
```text
baby-feeding-tracker/
├── backend/
│   ├── database.py
│   ├── enums.py
│   ├── feeds.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── frontend/               # (Coming soon - Vue.js)
├── feeding.db              # SQLite DB (auto-created)
├── .gitignore
├── requirements.txt
└── README.md
```
</details>

## ⚙️ Setup Instructions

Follow these steps to get the project running locally:

### 1. Clone the repository

bash
git clone https://github.com/your-username/baby-feeding-tracker.git
cd baby-feeding-tracker

### 2. Create and activate a virtual environment (recommended)
bash
Copy
Edit

#### On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

#### On Windows
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

If you don’t have a requirements.txt, run this to generate one:

bash
Copy
Edit
pip freeze > requirements.txt

### 4. Run the FastAPI server
  bash
  Copy
  Edit
  uvicorn main:app --reload
  By default, this runs the app at:

📍 http://127.0.0.1:8000

### 5. Access the API docs
  Open your browser to:
  
  Swagger UI: http://127.0.0.1:8000/docs
  
#💡Tips:

Your database (.sqlite3) file will be created automatically on first run if you’re using SQLite.

If you make schema changes, you may need to delete and recreate the database for now.

To exit the virtual environment: deactivate

yaml
Copy
Edit






