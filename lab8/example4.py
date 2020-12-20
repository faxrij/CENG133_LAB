def binary_to_dec(num1):
 
  sum = 0
  for i in range(len(num1)):
    b = num1[-1]
    c = int(b)*(2**i)
    sum+=c
    num1=int(num1)
    num1//=10
    num1 = str(num1)
  return sum

def dec_to_binary(num2):
    number = 0
    list_ = []
    while True:
        c = num2%2
        list_.append(c)
        num2//=2
        if num2==0:
            break
    c = []
    for i in range(len(list_)-1,-1,-1):
        c.append(list_[i])
    a = ''
    for j in c:
        j = str(j)
        a+=j
    return a
print(binary_to_dec('101111'))
