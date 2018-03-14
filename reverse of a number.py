n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    print('dig:',dig)
    rev=rev*10+dig
    print('rev:',rev)
    n=n//10
    print('n:',n)
print("Reverse of the number:",rev)
