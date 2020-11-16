evens=0
numbers=int(input())
for i in range(numbers):
  number = int(input())
  if number%2==0:
    evens+=1
  else:
    pass
percentage = (evens/numbers)*100
print(percentage)
