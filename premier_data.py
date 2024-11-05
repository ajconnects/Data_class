import pandas as pd

#open with normal open file
# filename = 'premier-league-matches.csv'

# with open(filename, mode='r') as file:
#     read_file = file.read()
# print(read_file)

#it read both csv and txt
filename = "premier-league-matches.csv"
file = pd.read_csv(filename)
print(type(file))
print(file)