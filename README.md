1. Clone the repository locally using this command in the command prompt:
  git clone https://github.com/stoyanadov/student_management_system.git
  Navigate to the project directory cd student_management_system

2. Create a virtual environment:
  On macOS/Linux:
    python3 -m venv .venv
  On Windows:
    python -m venv .venv

3. Activate the virtual environment:
  On macOS/Linux:
    source .venv/bin/activate
  On Windows:
    .venv\Scripts\activate

4. Install dependencies from requirements.txt:
   pip install -r requirements.txt

5. Connect to the PostgreSQL database

6. Apply migrations:
  python manage.py makemigrations
  python manage.py migrate

7. Run the server:
  python manage.py runserver

8. You can test the project by logging in the superuser:
username - admin
email - admin@admin.admin
password - admin
