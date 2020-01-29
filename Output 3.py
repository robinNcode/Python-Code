r=40

for i in range(1,r,1):
	print("-",end = '')

for i in range(1,6,1):
	print()
	if i==1:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==10:
				print("R",end='')
			elif j==11:
				print("o",end='')
			elif j==12:
			    print("b",end='')
			elif j==13:
				print("e",end='')
			elif j==14:
				print("r",end='')
			elif j==15:
				print("t",end='')
			elif j==16:
				print("o",end='')
			else:
				print(" ",end='')
	elif i==3:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==10:
				print("5",end='')
			elif j==11:
				print("7",end='')
			elif j==12:
			    print("8",end='')
			elif j==13:
				print("6",end='')
			else:
				print(" ",end='')
	elif i==5:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==10:
				print("U",end='')
			elif j==11:
				print("N",end='')
			elif j==12:
			    print("I",end='')
			elif j==13:
				print("F",end='')
			elif j==14:
				print("E",end='')
			elif j==15:
				print("I",end='')
			else:
				print(" ",end='')
	else:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			else:
				print(" ",end='')
		
					
print()
			
for i in range(1,r,1):
	print("-",end = '')
	
print()