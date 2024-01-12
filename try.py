try:
    limit=int(input("enter the number which you want to sum up the factorial"))
    factorial=1
    while(limit>0):
        factorial*=limit
        limit-=1
    print(factorial)
    if limit<0:
        raise Exception("ss")
except:
    if limit<0:
        raise Exception("negative value is not allowed")

