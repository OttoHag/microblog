# Microblog

A personal Flask project developed by Geir Otto Hag — focused on login functionality, form handling, and database integration. Built for learning, exploration, and sharing.

## 🚀 Features

- User login with Flask-WTF and validation
- Jinja2 templates with `base.html` and inheritance
- SQLAlchemy models and database migration
- Blueprint structure using the `create_app()` pattern
- Ready for expansion with registration, profile pages, and more

## 🛠️ Technologies

- Python 3.x
- Flask
- Flask-WTF
- SQLAlchemy
- Jinja2
- Bootstrap (optional for styling)

## 📦 Installation

```bash
git clone https://github.com/OttoHag/microblog.git
cd microblog
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
flask run
