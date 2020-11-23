#mail = input('enter mail: ')

ref = 'c.e.n.g113@example.com'
mail = ref
mail = mail.lower()
mail = mail.split("@")
first_part = mail[0]
second_part = mail[1]

first_part.replace("."," ")
if first_part+'@'+second_part==ref:
  print('Correct!')
else:
  print('Wrong!')