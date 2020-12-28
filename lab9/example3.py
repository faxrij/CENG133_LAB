def evens(n):
    count=0
    if len(n)==0:
        return 0
    else:
        if n.pop()%2==0:
            count=1
    return count + evens(n)


print(evens([1,2,3,4]))