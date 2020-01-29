
while 1:
	a=int(input())
	b=int(input())
	
	if a==0 or b==0:
		break;
		
	elif a>0 and b>0:
		print("primeiro")
		
	elif a>0 and b<0:
		print("quarto")
		
	elif a<0 and b<0:
		print("terceiro")
		
	else:
		print("segundo")