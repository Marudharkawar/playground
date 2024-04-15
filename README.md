## Introduction

Welcome to Playground! This is a Django project designed to provide api for product registration

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Set Up Virtual Environment

It's recommended to use a virtual environment to manage dependencies for Python projects. If you don't have virtualenv installed, you can install it using pip:

#### pip install virtualenv

Create a virtual environment for the project:

#### virtualenv venv

Activate the virtual environment:

On Windows:

#### venv\Scripts\activate

On macOS/Linux:

#### source venv/bin/activate

### 2. Install Python

If you haven't already installed Python, download and install the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 3. Clone the Repository

Clone the project repository from GitHub:

#### git clone https://github.com/Marudharkawar/playground.git
#### cd playgroung

### 4. Install Dependencies

Install project dependencies listed in the requirements.txt file:

#### pip install -r requirements.txt

### 5. Database Setup

Configure the database settings in the settings.py file located in the project_name directory. By default, the project is configured to use SQLite, but you can modify the settings for other databases such as PostgreSQL or MySQL.

Run migrations to create database schema:

#### python manage.py migrate

### 6. Create Superuser (Optional)

If you want to access the Django admin interface, you can create a superuser:

#### python manage.py createsuperuser

### 7. Run Development Server

Start the Django development server:

#### python manage.py runserver

Access the project in your web browser at http://localhost:8000.

### 8. API Endpoints

The following API endpoints are available:

#### List Products: GET /api/products/
#### Retrieve Product: GET /api/products/<id>/
#### Create Product: POST /api/products/
#### Update Product: PATCH /api/products/<id>/
#### Delete Product: DELETE /api/products/<id>/

To use filtering option , append field and value to list product endpoint like below

#### GET /api/products/?name=test&category=physical
Additional Notes
If you encounter any issues during setup or have questions, feel free to contact.
For more information about Django, visit the Django documentation.
