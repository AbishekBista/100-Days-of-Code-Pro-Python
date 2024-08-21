import pandas

data = pandas.read_csv('squirrel-count.csv')

grey_squirrel_data = len(data[data["Primary Fur Color"] == "Gray"])

black_squirrel_data = len(data[data["Primary Fur Color"] == "Black"])

red_squirrel_data = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    'Fur Color': ['Gray', 'Black', 'Red'],
    'Count': [grey_squirrel_data, black_squirrel_data, red_squirrel_data]
}

squirrel_df = pandas.DataFrame(data_dict)

squirrel_df.to_csv('squirrel-count-fur.csv')


