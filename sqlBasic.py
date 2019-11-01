from guizero import App, PushButton
import sqlite3

database = 'world.db' # create variable name for data base

conn = sqlite3.connect(database) # connect/open to data base


def Select_population():
    record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000 ORDER BY Name;')
    printer(record)

def Life_expectancy():
    record = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 60 ORDER BY Name;')
    for row in record:
        print(row)

def Gov_form():
    record = conn.execute('SELECT Name, GovernmentForm, Continent, LifeExpectancy FROM Country ORDER BY Name;')


#record = conn.execute('SELECT * FROM Country;')
record = conn.execute('SELECT Name, IndepYear, Population, LifeExpectancy FROM Country WHERE IndepYear >1900 ORDER BY IndepYear;')




app = App(title='Function Thingy')
button1 = PushButton(app, text='population less than 1 million', command='Select_population')
button2 = PushButton(app, text='life expectancy more than 60', command='Life_expectancy')
button3 = PushButton(app, text='type of government')
button4 = PushButton(app, text='independence gained after 1900')
app.display()


conn.close()