r=40

for i in range(1,r,1):
	print("-",end = '')

for i in range(1,6,1):
	print()
	if i==1:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==2:
				print("x",end='')
			elif j==4:
				print("=",end='')
			elif j==6:
			    print("3",end='')
			elif j==7:
				print("5",end='')
			else:
				print(" ",end='')
	elif i==3:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==17:
				print("x",end='')
			elif j==19:
				print("=",end='')
			elif j==21:
			    print("3",end='')
			elif j==22:
				print("5",end='')
			else:
				print(" ",end='')
	elif i==5:
		for j in range(1,r,1):
			if j==1 or j==39:
				print("|",end='')
			elif j==33:
				print("x",end='')
			elif j==35:
				print("=",end='')
			elif j==37:
			    print("3",end='')
			elif j==38:
				print("5",end='')
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