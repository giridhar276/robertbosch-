# Flask Web Project: Employee Directory

A simple Flask application that allows participants to:

- View employees
- Add an employee
- Delete an employee
- Understand routes, templates, static files and forms

This project intentionally stores data in a Python list to keep the Flask concepts simple.

## Setup

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python run.py
```

Open:

`http://127.0.0.1:5000`

## Main Concepts

- `app/__init__.py`: creates the Flask application
- `app/routes.py`: URL routes and request handling
- `app/templates`: HTML pages
- `app/static`: CSS
- `run.py`: starts the application
