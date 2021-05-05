file = open('firstFile.txt', 'r+')
file2 = open('secondFile.txt', 'a')

file.write("This is the python file operation")
file2.write("Hello world")

for each in file:
    print(each)