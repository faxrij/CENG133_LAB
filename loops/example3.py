low = 2
high = 20

for i in range(low,high+1):
  for j in range(2,i):
    if i%j==0:
      print(i,'not prime')
      break
  else:
    print(i,'prime')