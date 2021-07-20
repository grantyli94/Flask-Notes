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
    
    notes = db.relationship('Note', backref='user')

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

    # start_authenticate
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = cls.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        else:
            return False
    # end_authenticate


class Note(db.Model):
    """User notes"""

    __tablename__ = "notes"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(100), 
                      nullable=False)
    content = db.Column(db.String, 
                        nullable=False)
    owner = db.Column(db.String, 
                      db.ForeignKey('users.username'),
                      nullable=False)