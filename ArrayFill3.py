
n=float(input())

count=0
i=n
while i>0:
	print("N[",count,"] =","%.4f"%i)
	count+=1
	if count==100:
		break
	i/=2