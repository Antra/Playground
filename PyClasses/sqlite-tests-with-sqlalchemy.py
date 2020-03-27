import sqlite3
import sqlalchemy as db
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('sqlite-test.db')

print("** Starting direct SQL operations **")

c = conn.cursor()

c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')

c.execute('''
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
# conn.close()


c.execute('SELECT * FROM person')
print(c.fetchall())
c.execute('SELECT * FROM address')
print(c.fetchall())
conn.close()

print("** Done with direct SQL operations **")


# Let's use sqlalchemy instead to check the tables
engine = db.create_engine('sqlite:///sqlite-test.db')
connection = engine.connect()
metadata = db.MetaData()
person = db.Table('person', metadata, autoload=True, autoload_with=engine)
address = db.Table('address', metadata, autoload=True, autoload_with=engine)

print(person.columns.keys())
print(address.columns.keys())

print(repr(metadata.tables['person']))
print(repr(metadata.tables['address']))

# Equivalent to 'SELECT * FROM person'
query = db.select([person])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("This is equivalent to 'SELECT * FROM person'.")
print(ResultSet[:])

# Equivalent to 'SELECT * FROM person WHERE name is not null'
query = db.select([person]).where(person.columns.name != None)
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("This is equivalent to 'SELECT * FROM person WHERE name is not null'.")
print(ResultSet[:])


# Equivalent to 'SELECT * FROM person WHERE name is not null AND is not empty'
query = db.select([person]).where(
    db.and_(person.columns.name != None, person.columns.name != ''))
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("This is equivalent to 'SELECT * FROM person WHERE name is not null AND is not empty'.")
print(ResultSet[:])

# Equivalent to SELECT * FROM person ORDER BY id DESC'
query = db.select([person]).order_by(db.desc(person.columns.id))
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("This is equivalent to 'SELECT * FROM person ORDER BY id DESC'.")
print(ResultSet[:])

# Joins can be done automatically if there is already a relationship (foreign key)
query = db.select([person.columns.name,
                   address.columns.street_name, address.columns.street_number])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("This is an auto-join of person.name, address.street_name, address.street_number'.")
print(ResultSet[:])

# Joins can also be done manually if needs be
query = db.select([person, address])
query = query.select_from(person.join(
    address, person.columns.id == address.columns.person_id))
results = connection.execute(query).fetchall()
print("This is a manual join of person and address'.")
print(results)

# Create tables - fails silently if the table already exists.
emp = db.Table('emp', metadata,
               db.Column('Id', db.Integer()),
               db.Column('name', db.String(255), nullable=False),
               db.Column('salary', db.Float(), default=100.0),
               db.Column('active', db.Boolean(), default=True)
               )
metadata.create_all(engine)  # Creates the table

# Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen',
                              salary=60000.00, active=True)
ResultProxy = connection.execute(query)

# Inserting many records at ones
query = db.insert(emp)
values_list = [{'Id': '2', 'name': 'ram', 'salary': 80000, 'active': False},
               {'Id': '3', 'name': 'ramesh', 'salary': 70000, 'active': True}]
ResultProxy = connection.execute(query, values_list)

results = connection.execute(db.select([emp])).fetchall()
print(results)

# Updating values
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
results = connection.execute(db.select([emp])).fetchall()
print(results)
# Build a statement to update the salary to 100000
query = db.update(emp).values(salary=100000)
query = query.where(emp.columns.Id == 1)
results = connection.execute(query)
results = connection.execute(db.select([emp])).fetchall()
print(results)


# Deleting rows
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
# Build a statement to delete where salary < 100000
query = db.delete(emp)
query = query.where(emp.columns.salary < 100000)
results = connection.execute(query)
print("Deleting where salary < 100000'.")
results = connection.execute(db.select([emp])).fetchall()
print(results)

# Dropping a table
print("Dropping table 'emp'.")
emp.drop(engine)  # drops a single table
print("Dropping all tables.")
metadata.drop_all(engine)  # drops all the tables in the database
