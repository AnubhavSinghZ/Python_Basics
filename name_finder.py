import csv
search_name = input("Enter name to search: ")

with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0].lower() == search_name.lower():
            print("Found match:", row)
