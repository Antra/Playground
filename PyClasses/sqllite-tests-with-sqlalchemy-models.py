import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# The Echo flag will show the created SQL as well
engine = db.create_engine('sqlite:///:memory:', echo=True)
# Create a Session factory for future DB-sessions
Session = sessionmaker(bind=engine)

# See: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    #id = Column(Integer, primary_key=True)
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"


# Create the tables
Base.metadata.create_all(engine)


# Instantiate the user class
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

print(ed_user.name)  # 'ed'
print(ed_user.nickname)  # 'edsnickname'
print(str(ed_user.id))  # None


# Communicate with the database
session = Session()
ed_user = User(name='ed', fullname='Ed Jones',
               nickname='edsnickname')  # repeated for clarity
session.add(ed_user)

print(ed_user.id)
our_user = session.query(User).filter_by(name='ed').first()
print(ed_user.id)
print(our_user)
print("Is 'our_user' really the same as 'ed_user'?", our_user is ed_user)

# Add multiple users at the same time
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
# and then update the nickname
ed_user.nickname = 'eddie'

print("Is the session clean and up-to-date?")
print(
    f"If the session is clean and has no pending updates, then 'dirty' is empty: {session.dirty}")
print(
    f"If the session is clean and has no pending additions, then 'new' is empty: {session.new}")

# Let's commit those changes
session.commit()

print("Is the session clean and up-to-date?")
print(
    f"If the session is clean and has no pending updates, then 'dirty' is empty: {session.dirty}")
print(
    f"If the session is clean and has no pending additions, then 'new' is empty: {session.new}")

# Rolling back -- first to add some data
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)

# Querying the session shows the data is flushed
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

# Rolling back will show we're back to before
session.rollback()
print(ed_user.name)
print(fake_user in session)
# A SELECT will show the same (=only returns 'ed')
print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())


# Querying
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)


# Foreign keys and relationships
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

# Adding objects
jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
print(jack.addresses)

jack.addresses = [Address(email_address='jack@google.com'),
                  Address(email_address='j25@yahoo.com')]

# Demonstrate the bidirectional relationship
print(jack.addresses[1])
print(jack.addresses[1].user)

session.add(jack)
session.commit()
