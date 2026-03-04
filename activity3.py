n=int(input("enter the number;  "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not amstrong number")