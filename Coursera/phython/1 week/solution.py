import sys


a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

print(0.5*(-b + (b**2 - 4*a*c)**0.5))
print(0.5*(-b - (b**2 - 4*a*c)**0.5))