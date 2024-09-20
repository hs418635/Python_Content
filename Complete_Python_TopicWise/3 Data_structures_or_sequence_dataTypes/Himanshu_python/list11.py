##list=[]
##for i in range(10):
##    n=input("Enter your number")
##    list.append(n)
##print(list)
##a=int(input("Enter the number to check:"))
##
##i=0
##while i<len(list):
##    if list[i]==a:
##        print("number is available inside list")
##    else:
##        i=i+1

l=[1,2,3,4,5,67,89]
a=int(input("Enter the number to check:"))
def find(a,l):
    i=0
    while i< len(l):
        if l[i]==a:
            return i
        i+=1
        return -1

i=find(a,l)

if i!=-1:
    print("element is preset")
else:
    print("element not found")
        
