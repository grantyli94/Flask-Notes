from app import app
from models import db, User

db.drop_all()
db.create_all()

user1 = User(
    username="TestUser1",
    password="password1",
    email='test1@gmail.com',
    first_name='Test1',
    last_name='User1'
)

user2 = User(
    username="TestUser2",
    password="password2",
    email='test2@gmail.com',
    first_name='Test2',
    last_name='User2'
)

db.session.add_all([user1, user2])
db.session.commit()