age = int(input("Enter your age \n"))
normal_price = 3
if age>60 or age<6:
  print("Your ticket is free")
elif age>6 and age<18:
  normal_price = normal_price * 50/100
  print("Your ticket price is " , normal_price)
else:
  print("Your ticket price is ", normal_price)