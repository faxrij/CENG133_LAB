def get_password_level(pw):
  letters = 0
  spec_char = 0
  number = 0
  level = 0
  if len(pw) < 8 or " " in pw:
      return(level)
  for char in pw:
    if char.isalpha():
      letters += 1
    elif char.isnumeric():
      number += 1
    else:
      spec_char += 1
  if letters != 0:
    level += 1
  if number != 0:
    level += 1
  if spec_char != 0:
    level += 1
  return(level)

def main():
  pw = input("Enter password: ")
  print("Security level: ", get_password_level(pw))
main()
