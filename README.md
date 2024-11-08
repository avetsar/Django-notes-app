# Django-notes-app
# Notes App

This is a simple notes management application built with Django, Flask, and SQLite. The project allows users to create, edit, and view notes. Django is used for the main application with an admin interface, while Flask provides an API for accessing notes in JSON format.

## Project Structure

- **Django**: Manages the main application, including an admin interface for CRUD operations on notes.
- **Flask**: Provides a simple API to retrieve notes in JSON format.
- **SQLite**: Used as the database to store notes data.

## Features

- **Django Admin Interface**: Easily add, update, delete, and view notes.
- **Flask API**: Access notes via API in JSON format.
- **SQLite Database**: Stores note data persistently.

## Getting Started

### Prerequisites

- Python 3.8+
- Django
- Flask
- SQLite (default in Python)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/notes-app.git
   cd notes-app
2.Set up a virtual environment and activate it:

python -m venv venv

source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
3.Install the required packages:

pip install -r requirements.txt

4.Navigate to the Django project directory:

cd notes_project
5.Apply Django migrations:

python manage.py makemigrations
python manage.py migrate
6.Create a Django superuser to access the admin panel:

python manage.py createsuperuser

### Running the Project
Start Django Server
1.In the notes_project directory, start the Django development server:

python manage.py runserver

2.Visit the Django admin interface at http://127.0.0.1:8000/admin and log in with your superuser credentials.

Start Flask API Server
1.Open a new terminal, activate the virtual environment, and navigate to the Flask app directory:

cd flask_app
python app.py

2.The Flask API will be available at http://127.0.0.1:5000/api/notes.

Project Structure

notes-app/
├── flask_app/              # Flask app directory
│   └── app.py              # Flask API code
├── notes_project/          # Django project directory
│   ├── db.sqlite3          # SQLite database file
│   ├── notes/              # Notes app directory
│   ├── manage.py           # Django management script
│   └── notes_project/      # Django project settings
├── requirements.txt        # Project dependencies
└── .gitignore              # Git ignore file
API Usage
The Flask API provides the following endpoint:

GET /api/notes: Returns a JSON list of all notes.
Example response:

json
```
[
    {
        "id": 1,
        "title": "Sample Note",
        "content": "This is a sample note content."
    },
    {
        "id": 2,
        "title": "Another Note",
        "content": "More note content here."
    }
]
```
