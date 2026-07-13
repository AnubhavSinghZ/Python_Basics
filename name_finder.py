import csv
find_name = input("Enter name to search: ")

with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0].lower() == find_name.lower():
            print("Found match:", row)
