n=int(input("enter the number : "))
m=str(n)
r=m[::-1]
l=int(r)
if l==n:
    print("palindrome")
else:
    print("Not palindrome")
