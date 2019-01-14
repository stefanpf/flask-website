# flask-website

The code that powers my personal website, stefanpfeuffer.com

Built with Python, HTML5, CSS3, and a tiny bit of JavaScript.

## Installation

To install and test:

1. Download or clone the repository.

2. Install all necessary dependencies:

```
pip install -r requirements.txt
```

You may want to initialize a virtual environment before doing this.

3. From the repository's root directory initialize a database:

```
flask db init
```

4. Migrate the database models to the new database:

```
flask db migrate -m "add users and posts tables"
```

5. Upgrade the databases with these tables:

```
flask db upgrade
```

6. From the repository's root directory start a Flask shell with `flask shell` and add a user to the database:

```python
user = User(username='testuser', email='test@company.com')
user.set_password('test123')
db.session.add(user)
db.session.commit()
exit()
```

7. Start up the Flask development webserver:

```
flask run
```

8. Open a browser and go to `localhost:5000` to test the visitor-facing frontend.

9. Go to `localhost:5000/auth/login/` and login with the email and password you set in step 6.) to see the admin dashboard.
