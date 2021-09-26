import csv
rows = []

with open("./Data Set.csv") as file:
    for row in file:
        rows.append(row)

print(rows)
