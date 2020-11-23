name = input('Enter your name:')
for i in name:
  print(i.upper())
sum = ''
condition = True
while condition:
  string = input('Please enter any string: ')
  if string!='quit':
    sum+=string
  
  elif string=='quit':
    print(sum)
    break
