from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    
    """Site user"""

    __tablename__ = "users"

    username = db.Column(db.String(20),
                         primary_key=True)
    password = db.Column(db.Text,
                         nullable=False)
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=True)
    first_name = db.Column(db.String(30),
                           nullable=False)
    last_name = db.Column(db.String(30),
                          nullable=False)

    def __repr__(self):
        """Shows information about user"""

        return f'<{self.username}, {self.first_name}, {self.last_name}>'

    # start_register
    @classmethod
    def register(cls, username, pwd, first_name, last_name, email):
        """ register user w/hashed password & return user."""
        hashed = bcrypt.generate_password_hash(pwd).decode('utf8')

        return cls(username=username,
                   password=hashed,
                   first_name=first_name,
                   last_name=last_name,
                   email=email)
    # end_register
