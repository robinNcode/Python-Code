
n=int(input("Input a integer num:"))

sum=0
temp=n

while temp!=0:
	r=int(temp%10)
	sum=sum+r
	temp=temp/10
	
print("Sum of all digits is =",sum)