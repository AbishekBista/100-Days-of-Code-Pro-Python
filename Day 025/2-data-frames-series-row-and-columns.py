import pandas

data = pandas.read_csv("weather-data.csv")


data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())

print(data["temp"].max())

# Get data in columns
print(data["condition"])

print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_in_f = int(monday.temp) * 9 / 5 + 32
print(monday_temp_in_f)


# Create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')