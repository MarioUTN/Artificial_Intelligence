import pandas as pandas

names = ['Juan', 'Martha', 'Pedro', 'Jorge', 'Blass', 'Lisa', 'Antony']
ages = [23, 78, 22, 19, 45, 33, 20]
gender = ['Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male']
province = ['Burgos', 'Madrid', 'Toledo', 'Burgos', 'Madrid', 'Toledo', 'Madrid']
sons = [2, 0, 0, 3, 2, 1, 4]
pets = [5, 1, 0, 5, 2, 2, 3]

list = {'Names': names, 'Ages': ages, 'Gender': gender, 'Province': province, 'Sons': sons, 'Pets': pets}

print(list)

dataframe = pandas.DataFrame(list)
print(dataframe)
