password = 'abc123'
your_password = input('Enter ')
while your_password!=password:
  print('your password is incorrect, try again')
  your_password = input('Enter again: ')
  if your_password=='help':
    print(password[0])
  elif your_password==password:
    print('Yes')
    break