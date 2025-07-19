# Job Applicant Dashboard (Junior Developer)

## Features
- Applicant list view with CTA buttons
- Detail portfolio page
- Delete user + portfolio

## Setup Instructions

```bash
# Clone
git clone https://github.com/c4sTILLow/Job-Applicant-Dashboard.git
cd Job-Applicant-Dashboard

# Create virtualenv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip freeze > requirements.txt

# Migrate
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Commit
git commit -m "feat: create applicant list view using Bootstrap table"
git commit -m "fix: correct get_object method signature in detail view"
git commit -m "wip: building delete functionality for applicant"
git commit -m "bug: resolve template not found error for detail page"

# Run
python manage.py runserver
