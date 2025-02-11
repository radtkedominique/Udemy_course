from csv import reader

with open('/Users/dominique.radtke/Documents/DHBW/playlist csv/BibizaCO1.csv') as file:
    csv_reader = reader(file, delimiter=',')
    for row in csv_reader:
        print(row)



from csv import DictReader

with open('/Users/dominique.radtke/Documents/DHBW/playlist csv/BibizaCO1.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row)

from csv import DictWriter
with open('Users/dominique.radtke/Documents/test.csv', 'w') as file:
    headers = ['Name', 'Age']
    csv_writer_dict = DictWriter(file, fieldnames=headers)
    csv_writer_dict.writeheader()
    csv_writer_dict.writerows({'Name': 'Nique', 'Age': '22'})


import pickle
blue = Cat()
with open('pets.pickle', 'wb') as file:
    pickle.dump(blue, file)

with open('pets.pickle', 'rb') as file:
    zombie = pickle.load(file) #get the pickled data back out
    

