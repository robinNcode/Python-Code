r=40

for i in range(1,r,1):
	print("-",end = '')

for i in range(1,6,1):
	print()
	
	for j in range(1,r,1):
		
		if j==1 or j==39:
			print("|",end='')
		else:
			print(" ",end='')

print()
			
for i in range(1,r,1):
	print("-",end = '')
	
print()
