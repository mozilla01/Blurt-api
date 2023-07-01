REST API for the Twitter clone :D

### Setup:

**Requirements** : Have Python (>3.4) installed

1. Clone the repo
2. Inside the cloned folder, create a virtual environment using
   ```
   python3 -m venv .env
   ```
3. Activate the environment
   - If using a bash shell
   ```
   source env.sh
   ```
   - Else
   ```
   .env/scripts/activate
   ```
4. Install all dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run migrations for essential tables like sessions, auth, etc
   ```
   python manage.py migrate
   ```
6. Finally, run the server
   ```
   python manage.py runserver
   ```
