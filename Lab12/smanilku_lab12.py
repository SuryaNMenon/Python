# Name: Suryanarayan Menon Anilkumar
# Andrew ID: smanilku
# Code was guided by Claude AI

import os
import re
import sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("--- Problem 1 ---")
connection = sqlite3.connect('dogsdb.sqlite3')
cursor = connection.cursor()
query = 'select name from sqlite_master where type="table"'
cursor.execute(query)
table = cursor.fetchall()
print(table)

print("\n--- Problem 2 ---")
query = 'select * from dogs'
cursor.execute(query)
table = cursor.fetchall()
print(table)
print(type(table))
for row in table:
    print(row)

print("\n--- Problem 3 ---")
print(cursor.description)
for col in cursor.description:
    print(col[0])
colnames = []
for col in cursor.description:
    colnames.append(col[0])
print(colnames)

print("\n--- Problem 5 ---")
breeds = [ ['Mutt', 'Mangy and skinny'], 
          ['Boxer', 'Short, always looks grumpy'],
 ['Pekingese', 'Not really a dog'], ['Basset', 'So much skin'],
['Beagle', 'Cute-ish'], ['Irish_Setter', 'Drinks your whiskey'], ['Terrier',
'Fetch, boy'], ['Whippet', 'Whippet good'], ['Yorkie', 'Cute'], ['Gread Dane',
'So huuuge'], ['Akita', 'or is it Atika?'], ['Great Dane', 'Not that great']]
print(breeds)

print("\n--- Problem 6 ---")
cursor.execute('drop table if exists Breeds')
cursor.execute('create table Breeds (Breed VARCHAR(20), Description VARCHAR(40))')
cursor.executemany('insert into Breeds values (?, ?)', breeds)
connection.commit()
cursor.execute('select name from sqlite_master where type="table"')
print(cursor.fetchall())

print("\n--- Problem 7 ---")
cursor.execute('select * from Breeds')
for row in cursor.fetchall():
    print(row)

print("\n--- Problem 8 ---")
query = '''select dogs.Name, dogs.Breed, Breeds.Description
           from dogs join Breeds on dogs.Breed = Breeds.Breed'''
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

print("\n--- Problem 9 ---")
query = 'select Name, Age from dogs where Age >= 5'
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

print("\n--- Problem 10 ---")
cursor.execute('select AVG(dogs.Age) from dogs')
average = cursor.fetchone()[0]
print(f"Average age of dogs: {average:.2f}")

connection.close()

print("\n--- Problem 11 ---")
with open('testdata.txt') as file:
    lines = file.read().splitlines()
print(lines)

patterns = [
    r'\d',
    r'[A-Za-z]',
    r'\b[-+]?\d+\b',
    r'^a',
    r's$',
    r'\(',
    r'a.*e|e.*a',
    r'aeiou',
    r'a.*e.*i.*o.*u',
]

for pattern in patterns:
    print(f"Pattern: {pattern}")
    for line in lines:
        if re.search(pattern, line):
            print(f"Matched: {line}")
    print()
