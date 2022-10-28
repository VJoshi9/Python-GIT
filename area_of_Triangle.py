A = int(input("First side"))
B = int(input("Second side"))
C = int(input("Third side")) 
P = A+B+C
SP = P/2
#Heron's Formula (SP(SP-A)(SP-B)(SP-C))**0.5
Area = (SP*(SP-A)*(SP-B)*(SP-C))**0.5
print(Area)