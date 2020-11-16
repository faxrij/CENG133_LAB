number1 = int(input())
number2 = int(input())
match = 0
while number1>0 and number2>=0:
  if number1%10==number2%10:
    match+=1
  number1//=10
  number2//=10
print(match)
