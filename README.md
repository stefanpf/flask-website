# flask-website

The code that powers my personal website, stefanpfeuffer.com

Built with Python, HTML5, CSS3, and a tiny bit of JavaScript.

## Installation

To install and test:

1. Download or clone the repository.

2. Install all necessary dependencies:

    pip install -r requirements.txt

You may want to initialize a virtual environment before doing this.

3. From the repository's root directory initialize a database:

    flask db init

4. Migrate the database models into the new database:

    flask db migrate -m "add users and posts tables"

5. Upgrade the database with these tables:

    flask db upgrade

6. Start a Python shell and add a user to the database:

    $ ./python
    Python 3.7.1
    >>> user = User(username='yourusername', email='test@test.com')
    >>> user.set_password('test123')
    >>> db.session.add(user)
    >>> db.session.commit()
    >>> exit()

7. Start up the Flask development webserver:

    flask run

8. Open a browser and go to `localhost:5000` to see the visitor-facing front-end.

9. Go to `localhost:5000/auth/login` and login with the email and password you set in step 6. to see the admin dashboard.
