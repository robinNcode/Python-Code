#Multiplication Table With For Loop..

print("	::Maltiplication Table::	")

n=int(input())

sum=0

for i in range(1,11,1):
	sum=n*i
	print(n,"x",i,"=",sum)
	