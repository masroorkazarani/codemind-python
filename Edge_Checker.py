a,b = map(int,input().split())
if(a==1 and b==10 or b==1 and a==10 or a==b+1 or b==a+1):
    print("Yes")
else:
    print("No")