
#.read it read only once
filename = "source.txt"

file = open(filename, mode= 'r')
text = file.read()
print(text)
print(file.closed)

#using with to open file and write
with open(filename, mode= 'r+') as new_source:
    f_n = new_source.read()
print(f_n)
