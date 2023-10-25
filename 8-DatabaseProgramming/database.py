import sqlite3


class Persons():
    def __init__(self, IDNum=1, first="", last="", age=1):
        self.IDNum = IDNum
        self.first = first
        self.last = last
        self.age = age
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
    def LoadPerson(self, IDNum):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(IDNum))
        
        results = self.cursor.fetchone()
        
        self.IDNum = IDNum
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    def InserPerson(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ('{}', '{}', '{}', '{}')
        """.format(self.IDNum, self.first, self.last, self.age))
        
        self.conn.commit()

p1 = Persons(2, 'Daer', 'Rob', 33)
p1.InserPerson()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

conn.close()
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons(
#     id INTEGER PRIMARY KEY,
#     FirstName TEXT,
#     LastName TEXT,
#     age INTEGER
# )       
# """)

# cursor.execute("""
               
# INSERT INTO persons VALUES
# (1, 'Paul', 'Smith', 34),
# (3, 'Ren', 'Smith', 37),
# (4, 'Warr', 'Buff', 23)

# """)

# cursor.execute("""
# SELECt * FROM persons
# WHERE LastName = 'Smith'               
# """)

# rows = cursor.fetchall()
# print(rows)

# conn.commit()
# conn.close()

