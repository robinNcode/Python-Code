
s=0.0
b=1.0
c=1.0

for i in range(1,40,2):
	
	c=i/b
	s=s+c
	b*=2
	#print(i,"/",b,"=",c)

print("%.2f"%s)