import sqlite3
import pyttsx3

tts = pyttsx3.init()

database = 'world.db'

conn = sqlite3.connect(database)

#record = conn.execute("SELECT Name, HeadOfState FROM Country WHERE GovernmentForm = 'Republic' ORDER BY Name;")
#record = conn.execute("SELECT Name, GNP, Population FROM Country WHERE Population > 1000000000 ORDER BY Population;")
#record = conn.execute("SELECT Name, Population, SurfaceArea FROM Country WHERE SurfaceArea < 10000000 ORDER BY Population;")
record = conn.execute("SELECT Name, Population, SurfaceArea FROM Country WHERE SurfaceArea < 1000000000, Population > 1000000000;")

for row in record:
   print(row)
#   tts.say(row)
#   tts.runAndWait()


