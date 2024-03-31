import csv
import math
import random

names = [
    "Sophia Reynolds", "Ethan Hayes", "Isabella Palmer", "Mason Olson", "Olivia Tucker",
    "Aiden Carter", "Ava Patel", "Elijah Rivera", "Mia Evans", "Logan Mitchell",
    "Amelia Campbell", "Lucas Gonzales", "Harper Hughes", "Alexander Jenkins", "Charlotte Ross",
    "Benjamin Price", "Emma Collins", "William Cooper", "Emily Richardson", "James Howard",
    "Madison Ward", "Michael Adams", "Abigail Bailey", "Jacob Foster", "Elizabeth Murphy",
    "Daniel King", "Ella Sullivan", "Matthew Brooks", "Victoria Kelly", "Jackson Bennett",
    "Sofia Cooper", "David Parker", "Avery Harrison", "Joseph Gray", "Chloe Myers",
    "Alexander Woods", "Grace Brooks", "Samuel Watson", "Evelyn Phillips", "John Rogers",
    "Lily Marshall", "Christopher Reed", "Scarlett Coleman", "Ryan Diaz", "Anna Long",
    "Nicholas Gonzales", "Layla Russell", "Jonathan Hayes", "Natalie Hughes", "Joshua Thompson",
    "Hailey Richardson", "Andrew Bryant", "Amelia Murray", "William Harrison", "Aria Nelson",
    "Nathan Henderson", "Ella Jenkins", "Isaac Perry", "Sophie Perez", "Caleb Mitchell",
    "Mia Harrison", "Ethan Olson", "Luna Rivera", "Gabriel Campbell", "Avery Roberts",
    "Grace Davis", "David Peterson", "Stella Cook", "Jack Ward", "Hannah Allen",
    "Christopher Price", "Aurora Martinez", "Carter Baker", "Addison Powell", "Luke Bryant",
    "Eleanor Sullivan", "Michael Barnes", "Skylar Mitchell", "Lucas White", "Lillian Edwards",
    "Daniel Young", "Leah Collins", "Henry Howard", "Zoe Lewis", "Jack Cooper",
    "Nora Rivera", "Wyatt Bennett", "Ava Bryant", "Matthew Hughes", "Madeline Perry",
    "Liam Foster", "Olivia Parker", "Gabriel Campbell", "Emily Evans", "Daniel Carter",
    "Lily King", "Jackson Bell", "Charlotte Gray", "Jacob Wright", "Madison Allen"
]

with open('traveler_database.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'name', 'vector']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(names)):
        writer.writerow({'ID': i, 'name': names[i], 'vector': [random.random() for x in range(10)]})