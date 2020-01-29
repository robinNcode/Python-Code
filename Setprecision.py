
a=13.9477783499998807

print("a =",a)

print("a =","%.2f"%a,"using formatspecifier")

print("a =",round(a,3),"using round function")

print("a =","%.4f"%round(a,4),"using formatspecifier & round")

print("a =","{0:.5f}".format(a),"using format function")

print("a =","{0:.6f}".format(round(a,6)),"using Format&Round function")