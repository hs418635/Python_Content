'''#List-"which can strore multiple itmes"
l=list((2,3,4,4,5))#inbuilt list#
l=[1,2,3,4,5]#user defined list#
#duplications are allowed#Z

l=list((1,2,3,3,4,5,5,5,5,))#inbuilt list#
print(l)
l=[1,2,3,4,4,5,66,5,54]#user defined#
print(l)

            #Indexing are allowed #
l=list((2,3,4,5,6,7,8,9))
print(l[-1])
print(l[4])
print(l[0])
            #string slicing-to divide string in a particular manner#
l=[1,2,3,4,5,6,7,8,9,0,11,12,1,3,1,4]
print(l[:])
print(l[0:])
print(l[2:])
print(l[:4])
print(l[2:4])
print(l[1:6])

                #Nested list-list under list#
l=list((1,2,3,4,(3,4,5)))
print(l[3])
print(l[4])
print(l[4][2])
print(l[4][1])
print(l[4][0])



l=[1,2,3,4,5,6,[4,5,6,7,8,99,0]]
print(l[0])
print(l[1])
print(l[4])
print(l[5])
print(l[6][0])
print(l[6][4])
print(l[6][6])
print(l[6])





l=[1,2,3,4,5,6,7,[4,5,6,7,7,8,8,9]]
print(l[5])
print(l[4])
print(l[1])
print(l[7])
print(l[7][6])
print(l[7][7])
print(type(l))


a=list(("maddy",12,23,("hero",1/2,(34,55,40,99,87,87,))))
print(a[3])
print(a[0])
print(a[3][1])
print(type(a))
print(a[3][2][1])
print(a[3][2][4])





             #some inbuilt function of list#

a=[5,6,7,8,9,10]
b=[]
print(len(a))
print(max(a))
print(min(a))
print(type(a))
a.append(11)#append only takes one argument#
print(a)
a.insert(12,13)#insert only takes 2 argument#
print(a)
a.pop()#pop will automatically delete last value#
print()
a.remove(6)
print(a)
a.extend([89,90])
print(a)
a.reverse()
print(a)
b=a.copy()
print(b)
a.clear()
print(a)




a=[1,2,3,4,5,6,7]#user defined list#
print(type(a))

b=list((1,2,3,4,5,6,7))#inbuilt list#
print(type(b))


#list is indexed#
a=[3,4,5,6,7,8,8,6,5,4]
print(a[4])
print(a[7])


#nested list#
a=list((2,3,4,56,(4,2,5,6,7,(3,4,5,6))))
print(a[4][5][2])

a=list((1,2,3,4,"maddy","rishabh",(10,11,23,"bhagyashree",56,("hero","hi","hello"))))
print(a[6][3])
print(a[6][5][2])
print(a[6][4])


a=[1,2,3,4,5,6,7,["maddy","rishabh","bhagyashree","hero",[1,2,3,4,[5,6,7,8]]]]
print(a[7][2])


               #list slicing#
l=[1,2,3,4,5,6,"maddy","bhagyshree",8,9,0,10]
print(l[2:])
print(l[0:])
print(l[0:8])
#In list slicing it will take starting index but ended before ending index#
print(l[1:10])
print(l[:10])
#if we don't give starting index it will start from 0th index#

#negative index starts from -1(right) and postive index start from 0(left)#


l=[1,2,3,4,5,6,"maddy","bhagyshree",8,9,0,10]
print(l[-1])
print(l[0])

#list are mutable,because it has append function#
#mutable =changeable#


#some inbuilt funtion of list#


                    #appendd#
a=[2,3,4,5,6,7,8,"maddy",["rishabh","hero"],4,5,6,7]
#a.append("shree",7)#append always add value to the last and it will take only one argument#ERROR
a.append("shree")
print(a)

                #insert#


a=[2,3,4,5,6,7,8,"maddy",["rishabh","hero"],4,5,6,7]
a.insert(6,"shree")#first one is a index no and second one is value what we wanted to add#
print(a)


              #extend#
a=list((2,3,4,5,6,7,8,"maddy",["rishabh","hero"],4,5,6,7))
a.extend([2,3,"maddy","shree",4,5,6,7])
print(a)
a.extend([77,68,68,49])
print(a)
a.extend(["maddy","hero","jalandhar"])
print(a)


          #inbuilt function of python#

a=list(("maddy",1,3,4,5,6,7,(4,5,6,7,7,(5,6,7,8))))
print(len(a))
#element in nested list will be counted as one#

a=list(("maddy",1,3,4,5,6,7,[4,5,6,7,7,[5,6,7,8]]))
print(len(a))


a=[3,4,5,6,7,8,9,0,["maddy","rishabh",["hero","zero",["shreekant","dipika",["sarika"]]]]]
print(len(a))



a=[3,4,5,6,7,8,9,0]
print(max(a))
print(min(a))


a=["maddy","rishabh","hero","rishebh"]
print(max(a))
print(min(a))


#a=["maddy","rishabh","hero","rishebh",3]
a=["maddy","rishabh","hero","rishebh"]
print(max(a))#ERROR
print(min(a))


  #will give min() and max() only if there is only "int" or "string" otherwise it will give error#


#sum() will run in list but not in nested list#

a=[1,2,3,4,5,6]
print(sum(a))

#a=[1,2,3,4,5,6[6,7]]
a=[1,2,3,4,5,6,[6,7]]
print(sum(a))

#not for string#

a=["rishabh","maddy","hero",]
print(sum(a))

               #pop()#


a=list((2,3,4,5,6,7,8,("maddy","rishabh","hero",("hi","hello"))))
a.pop()
print(a)



a=list((2,3,4,5,6,7,8,["maddy","rishabh","hero"]))
a.pop()
print(a)


a=list((2,3,4,5,6,7,8,"maddy"))
a.pop()
print(a)

              #clear()#
a=[1,2,3,4,5,5,[6,7,8,9,9]]
a.clear()
print(a)

            #del()#
a=[5,6,7,8,9,["maddy","hero",["hi"]]]
a.append("rishabh")
print(a)
del a
print(a)


             #reverse()#

a=[3,4,5,6,["rishabh","maddy",["hi","hero"]]]
a.reverse()
print(a)

a=[3,4,5,6,"rishabh","maddy"]
a.reverse()
print(a)

a=[5,6,7,8,8]
a.reverse()
print(a)


           #copy()#


a=[]
b=["rishabh","maddy","hi","hello",2,3,4,5,6,7]
a=b.copy()
print(a)



a=list(())
b=["hi","hell0",4,5,6,7,8,]
a=b.copy()
print(a)


a=list((5,6,7,8,9,[4,5,"maddy",5,[5,6,7,[5,6,"hi"]]]))
b=[]
b=a.copy()
print(b)

               #remove()#
#this function only works in list not in nested list#

a=["rishabh","a","b"]
a.remove("a")
print(a)
a.remove("rishabh","b")#remove takes only one argument#ERROR
print(a)
a=[2,3,4,5]
a.pop()
print(a)
a.remove(5)
print(a)


                  #sort()#
#this funtion is used for ascending and descending order#

                #for ascending#

a=[1,2,4,5,3,77,81,11,5,6]
a.sort()
print(a)
                       #for descending#
a.sort(reverse=True)
print(a)



a=[4,5,6,56,78,12,80,7,8]
a.sort()
print(a)
a.sort(reverse=True)
print(a)


a=["rishabh","reshabh","hi","hello","yryryry"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
del a
print(a)
'''

               #index#  

a=[9,4,5,6,7,8]
print(a.index(7))

a=["maddy","rishabh",2,3,4,5,6,7,7]
print(a.index("rishabh"))


















