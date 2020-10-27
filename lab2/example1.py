a = int(input("Enter the a value : "))
b = int(input("Enter the b value : "))
c = int(input("Enter the c value : "))
d = (b**2 - 4*a*c)
if d>0:
  print("It has two real solutions")
if d==0:
  print("It has only one real solution")
if d<0:
  print("It does not have any real solutions")
