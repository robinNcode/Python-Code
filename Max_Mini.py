'''MsM Robin
   Sonargaon University
   Date:8/14/19
'''
a=int(input("Enter a value for A:"))

b=int(input("Enter a value for B:"))

c=int(input("Enter a value for C:"))

temp=max(a,b)
max=max(temp,c)

print("Maximum between A,B & C =",max)

temp2=min(a,b)
min=min(temp2,c)

print("Minimum between A,B & C =",min)
