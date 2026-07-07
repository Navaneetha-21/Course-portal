# 🎓 Course Portal

A web-based Course Portal developed using **Django** that allows users to browse, search, and view detailed information about various courses. The project demonstrates Django's Model-View-Template (MVT) architecture, template inheritance, static file management, and responsive web design.

---

## 📌 Features

- 📚 View all available courses
- 🔍 Search courses by title
- 📄 Course detail page
- 🧩 Reusable Navbar and Footer using template inheritance
- 🎨 Responsive user interface with HTML and CSS
- 📁 Static file management
- 🗄️ SQLite database integration
- ⚡ Clean and modular Django project structure

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- HTML5
- CSS3
- SQLite
- Git
- GitHub

---

## 📂 Project Structure

```
course_portal/
│
├── course/
│   ├── migrations/
│   ├── static/
│   │   └── course/
│   ├── templates/
│   │   └── course/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── partials/
│   │   ├── navbar.html
│   │   └── footer.html
│   └── base.html
│
├── static/
│   └── css/
│       └── style.css
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/course-portal.git
```

### 2. Navigate to the project

```bash
cd course-portal
```

### 3. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---



## 🚀 Future Enhancements

- User Authentication
- Student Dashboard
- Course Enrollment
- Instructor Portal
- Course Categories
- Pagination
- Course Ratings and Reviews
- Admin Analytics Dashboard

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Django MVT Architecture
- URL Routing
- Template Inheritance
- Static Files Management
- Django ORM
- SQLite Database
- CRUD Operations
- Search Functionality
- Responsive Web Design
- Git & GitHub Version Control

---

## 👨‍💻 Author

**Navaneeth Kotari**

- GitHub: https://github.com/Navaneetha-21

---

## 📄 License

This project is developed for learning and educational purposes.
