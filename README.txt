# TechLearn Academy
TechLearn Academy is a web-based learning platform built using **Python**, **Django**, and **SQLite**.  
The project provides a simple system where students can access learning resources and administrators can manage courses and users.

---

## 🚀 Features
- User registration and authentication
- Course management
- Organized learning resources
- Simple and clean UI
- SQLite database integration
- Django MVC architecture

---

## 🛠 Tech Stack
- **Backend:** Python
- **Framework:** Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap, Django Templates

---

## 📂 Project Structure
```
TechLearn-Academy/
│
├── manage.py
├── README.md
├── techlearn_academy/        # Main project configuration
├── courses/                  # Courses application
├── users/                    # User management
├── templates/                # Global templates
├── static/                   # Static files (CSS, JS, images)
└── db.sqlite3                # SQLite database
```

---

## ⚙️ Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/bahauddin1097/TechLearn-Academy.git
cd TechLearn-Academy
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate it:
**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### 3. Run Database Migrations
```bash
python manage.py migrate
```

### 4. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### 5. Start Development Server
```bash
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/
```

---

## 🔮 Future Improvements
- Implement **Django REST Framework API**
- Add **course enrollment system**
- Add **student progress tracking**
- Support **video lectures and file uploads**
- Build **student dashboard**
- Implement **course search and filtering**
- Add **email notifications**
- Improve UI using **Bootstrap or Tailwind CSS**
- Add **Docker support**
- Deploy on **AWS / Render / Railway**

---

## 📄 License
This project is open-source and available under the **MIT License**.
