import sqlite3

# create a name for the database
database = 'Company.db'

# create a connection to the database
conn = sqlite3.connect(database)

# conn.execute('DROP TABLE IF EXISTS Customers;')
#
# # create table with fields and data types
# conn.execute('''CREATE TABLE Customers
#             (id INT NOT NULL,
#              name TEXT NOT NULL,
#              age INT NOT NULL,
#              gender TEXT NOT NULL);''')

i = int(input('Press 1 to continue: '))

while i == 1:
    ids = input('Enter id: ')
    name = input('Enter name: ')
    age = input('Enter age: ')
    gender = input('Enter gender: ')

    myTuple = (ids, name, age, gender)

    # enter data values into the db
    conn.execute('''INSERT INTO Customers (id,name,age,gender) VALUES
                (?, ?, ?, ?);''', myTuple)

    # save changes into db
    conn.commit()

    i = int(input('Press 1 to continue: '))

# print results from query
records = conn.execute('SELECT * FROM Customers')
for rows in records:
    print(rows)

# closes the database so other programs can use it
conn.close()