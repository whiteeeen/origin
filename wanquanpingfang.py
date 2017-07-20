def isPerfect(n):
    i=0
    while i<=n:
        if i*i == n:
            return True
        i=i+1

flag=True
n=1
while flag:
    if isPerfect(n+100) and isPerfect(n+268):
        print(n)
        flag = False
    n=n+1

