# Job Applicant Dashboard (Junior Developer)

## Features
- Applicant list view with CTA buttons
- Detail portfolio page
- Delete user + portfolio

## Setup Instructions

```bash
# Clone
git clone https://github.com/yourusername/jobdashboard.git
cd jobdashboard

# Create virtualenv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Migrate
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run
python manage.py runserver
