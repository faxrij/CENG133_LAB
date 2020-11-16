password = 'abc123'
while True:
  enter = input("Enter a password ")
  if enter=='help':
    print('a')
  elif enter==password:
    print("Welcome ")
  else:
    print('Wrong ')
  break