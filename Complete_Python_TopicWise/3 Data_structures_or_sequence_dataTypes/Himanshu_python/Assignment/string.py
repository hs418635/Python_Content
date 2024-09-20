'''lis=[]
print(type(lis))

#inbuit
lis1=list()
print(type(lis1))

#user defined list
lis2=[1,2,3,4,5,6,7,8,9,10]
print(lis2)

'''lis3=['Robert',23,'indore']
print(lis3)
#inbuilt list with arguments
lis4=list(("himanshu","python"))
print(lis4)'''

print("length of lis2 is",len(lis2))

lis2.append(90)
print(lis2)
lis2.extend([11,13])
print(lis2)
lis2.insert(9,100)
print("lis2 is",lis2)

print(lis2.count(10))

lis2.reverse()
print("lis2 is :",lis2)

lis5=[]
lis2=[1,2,3,34]
lis5=lis2.copy()
print("lis5 is",lis5)

lis5.clear()
print("lis5 is",lis5)

lis3=[1,2,3,34]
lis3.pop()
print("removed value is:",lis3)

lis3.remove(3)
print("removed value is:",lis3)

#print("removed value is using remove is:"lis5.remove(100))
del lis3

print(lis3)'''


