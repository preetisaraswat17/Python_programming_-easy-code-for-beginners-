n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10 #pull out the last digit
    print('dig:',dig)
    rev=rev*10+dig  #save the last digit in rev
    print('rev:',rev)
    n=n//10 #remove last digit from original number
    print('n:',n)
print("Reverse of the number:",rev)
