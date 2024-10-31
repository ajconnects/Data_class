import pandas as pd
import numpy as np

product = ["rice", "bean", "garry", "soup"]
print(pd.Series(product))  #Series check the variable
print(type(pd.Series(product)))

num = np.array([44, 48, 94, 39])
d = pd.Series(num)
print(d.dtypes)

# for pandas will use dtype or dtypes to check the objects while for numpy will use type

print(d.size) #size it shows the size of objects in the Series

#name
print(d.name)  #the Series name was None
d.name = "num id"  #with the name will can assign a name to a product
print(d.name) #after assign a name to the product.
print(d)   #it carry the new name

#index -- allow you to refer to a position within a sequence
# we have two types of indexing the label-based(dict) indexing and the position based(list) indexing

worker = {'John': 56, 'William': 34, 'Daniel': 29, 'lucky': 56}
worker = pd.Series(worker)
print(worker.index) #it show the key values of the series
print(worker)
print('-'*50)
# label-based indexing can be call explicit (dict)
# position- based indexing can be call implicit (list) is the default indexing in pandas
#implicit
num_list = pd.Series([40,60,80,100,120], index= ['2', '4', '6', '8', '10'])
print(num_list['2'])
#print(num_list.iloc['4'])  #new feature to replace indexing

#explicit
num_dict = pd.Series({'Books': 30, 'Pen': 20, 'Note Pad': 50})
print(num_dict['Pen'])  #iloc dont work in strings
#print(num_dict.iloc['Pen'])

#using pandas mathematical methods sum(), max(), min(), idxmin(), idxmax() for numeric data
#while non mathematical methods head(), tail()
print(num_dict.idxmin())
print("*"*50)

#create a dataframe from a dictionary of list + specifies index
data = {"clothes": ['shirt', 'cap', 'jeans'],
        "shoes":  ['slip', 'canvas', 'nike']}

df = pd.DataFrame(data, index= [20.1, 30.1, 40.1])
print(df)

#create a dataframe from a list of dictionaries
data_list_d = [
        {'Name': 'Amy White', 'Age': 50, 'Working Experience (Yrs.)': 5 },
        {'Name': 'Jack Stewart', 'Age': 53, 'Working Experience (Yrs.)': 8 },
        {'Name': 'Richard Lauderdale', 'Age': 35, 'Working Experience (Yrs.)': 3 },
        {'Name': 'Sara Johnson', 'Age': 43, 'Working Experience (Yrs.)': 10 },
        ]

df = pd.DataFrame(data_list_d)
print(df)

#create a dataframe using a pandas series
ser_products = pd.Series(['Ipad', 'Iphone', 'IpadMini'])
ser_prices = pd.Series([344, 1992, 699])
#to add an index i have the same numbers of indices upon the creation of every series


data_a = {'Apple': ser_products, 'Prices': ser_prices}
df_a = pd.DataFrame(data_a)
print(df_a)

#professional of create a dataframe

df_1 = pd.DataFrame(
    data= [['Product A', 2444], ['Product B', 4774], ['Product C', 5684], ['Product D', 8475]],
    columns= ['ProductName', 'ProductPrice'],
    index= ['A', 'B', 'C', 'D'] )
print(df_1.shape)
print(df_1)
