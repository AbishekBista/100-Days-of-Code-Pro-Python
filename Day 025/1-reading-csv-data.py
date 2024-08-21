# with open('weather-data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temp = int(temp)
#             temperatures.append(temp)

            
#     print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")
# printing whole table
print(data)

# printing certain column
print(data["temp"])


