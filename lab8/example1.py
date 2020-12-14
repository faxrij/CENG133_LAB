
def sum_list(a_list):
  summ = 0 
  for i in a_list:
    summ+=i
  return summ

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(sum_list(a_list)**2)