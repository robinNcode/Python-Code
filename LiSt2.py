
subjects = ["C","C++","Java","Python","Android"]

print()
print(subjects)

print()
print("Before insert / append,Length of list is =",len(subjects))

subjects.append("Forturn")
subjects.insert(2,"Os")

print("	::Before Sort/Reverse::	")
i=0
while i<7:
	print(subjects[i])
	i+=1

subjects.reverse()

print()
print("	!! After Reverse !!	")
i=0
while i<7:
	print(subjects[i])
	i+=1
	
subjects.sort()

print()
print("	::After Sort::	")
i=0
while i<7:
	print(subjects[i])
	i+=1
	
print()
print("After insert / append,Length of list is =",len(subjects))

subjects.remove("Os")

print()

i=0
while i<6:
	print(subjects[i])
	i+=1

print()
print("After remove Length of list is =",len(subjects))

num=[1,45,67,88,99,66,77,22]

print()
print("	::Before Sort/Reverse/PoP::	")
i=0
while i<8:
	print(num[i])
	i+=1

num.reverse()

print()
print("	::After Reverse::	")
i=0
while i<8:
	print(num[i])
	i+=1

num.sort()

print()
print("	::After Sort::	")
i=0
while i<8:
	print(num[i])
	i+=1


num.pop()

print()
print("	::After PoP::	")
i=0
while i<7:
	print(num[i])
	i+=1
	
pos = num.index(67)
print()
print("Index of",num[4],"is =",pos)

num2 = [2,5,4,5,6,4,5,2,5,7,5]
print()
print("num2 =",num2)

count = num2.count(5)
print()
print("In this list",num2[1],"is reapeting",count,"times")

num2.clear()
print()
print("List of num2 after clear",num2)
