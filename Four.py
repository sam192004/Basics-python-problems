n1,n2,n3=map(int,input("Enter three numbers : ").split())
if n1>n2>n3:
    print(f"{n1} is greater")
elif n1<n2>n3:
    print(f"{n2} is greater")
else:
     print(f"{n3} is greater")
