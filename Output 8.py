from decimal import Decimal

a=234.345000
b=45.698000

print("%6f"%round(a,6),"-","%6f"%round(b,6))

print(round(a),"-",round(b))
print(round(a,1),"-",round(b,1))
print(round(a,2),"-",round(b,2))
print(round(a,3),"-",round(b,3))

print("%2e"% Decimal(a),"-","%2e"% Decimal(b))

print("%2E"% Decimal(a),"-","%2E"% Decimal(b))

print(a,"-",b)
print(a,"-",b)
