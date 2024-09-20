#Q1
'''a=[500,200,300,400,100]
a.sort()
a.reverse()
print(a)


#Q2
a=[1,2,3,4,5]
b=[8,54,45,12,78]
a=a+b
print(a)

#Q3
a=[1,2,3,4,5,6,7]
b=[]
for i in a:
    b.append(i**2)
print(b)
'''
#Q4
list1=[5,10,15,20,25,50,20]
b=list1.count(20)
if b!=0:
    print('"20" is present in the list ')
    c=list1.index(20)
    list1.pop(c)
    list1.insert(c,200)
    print(list1)
else:
    print(" 20 is not present in list ")
