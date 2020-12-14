def is_prime(num):
  for i in range(2,11):
    if num%i==0:
      return False
  else:
    return True

def print_primes_between(num,num2):
  for i in range(num,num2):
    if is_prime(i):
      print(i)

print(print_primes_between(5,18))