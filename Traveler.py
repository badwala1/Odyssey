from scipy import spatial
import csv
import pandas as pd

class Traveler:
    def __init__(self, data):
        self.data = data

    def get_ID(self):
        return self.data[0]

    def get_name(self):
        return self.data[1]

    def get_info_vector(self):
        raw = self.data[2:]
        return [eval(i) for i in raw]

    def find_event(self, event_file):
        traveler_vector = self.get_info_vector()
        event_vectors = []
        event_names = []
        events = []
        with open(event_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            headings = next(spamreader)
            for row in spamreader:
                event_names.append(row[1])
                events.append(row)
                event_vectors.append(list(map(float, row[2:-1])))

        tree = spatial.KDTree(event_vectors)

        return events[tree.query(traveler_vector)[1]][0]


t = []
with open('traveler_database.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    headings = next(spamreader)
    for row in spamreader:
        t.append(Traveler(row))

df_traveler = pd.read_csv ('traveler_database.csv')
df_event = pd.read_csv ('event_database.csv')

print(df_traveler)
print(df_event)

x = t[1]

liked = []
disliked = []

while(True):
    name = x.get_name()
    suggested = x.find_event("event_database.csv")
    print(name + " should do the following event: " + suggested)
    while(True):
        addTrip = input("Accept? (Y/N)")
        if(addTrip == "Y"):
            liked.append(suggested)
            break
        elif (addTrip == "N"):
            disliked.append(suggested)
            break
        else:
            print("Put a valid input.")
    end = input("Again? (Y/N)")
    if (end == "N"):
        break
    elif not (end == "Y"):
        print("Put a valid input.")

print(liked)
print(disliked)
