               #string slicing#
'''
a="hello ji ki haal chaal"
b="all is good"
print(b[:4]+b[4:7]+a[12:17]+a[17:23])



a="shreekant is a good boy"
b="rishabh is a bad boy"
print(a[0:10]+a[10:12]+a[12:15]+b[13:17]+b[17:20])
print(b[0:7]+a[8:11]+a[11:13]+a[15:20]+a[20:23])



a="my name is khan"
b=" and i am not a terrorist"
print(a[0:7])
print(a[0:17])
print(a[5:17])
print(a[:]+b[:])
print(a[:]+b[:10]+b[15:25])
print(b[5:9]+a[10:15])



a="hello how are u and"
b="I am fine"
print(a[0:6]+b[:])
print(b[5:10]+a[15:19]+a[13:15])

#single code will count one time in indexing#

a="India's economy is russia's economy is china's economy is"
b="not stable sustain very good"
print(a[0:19]+b[0:10])
print(a[19:39]+b[11:18])
print(a[39:57]+b[18:28])


#.will also count in indexing as one index#

a="how are u mr.sharma "
b="is fine"
print(a[10:20]+b[:])



     #list assignment#

a=[7,2,3,4,5,2,2,34,5,3,2]
print(type(a))
a.sort()
a.reverse()
print(a)




a=[4,2,3,6,7,81,33,2,4,5,7,223,3,45,667,3334,67]
a.sort()
a.reverse()
print(a)



          #concancate two list#


a=["rishabh",4,5,6,7,4,"alfonsa",45,56]
b=["maddy",55555555,44333,4444,5,]
print(a+b)






a=[1,2,3,4,5,6,7,66,7,67]
b=[5,6,7,8,8,888,23,3]
d=[6,5,6,7,8,6,4,3,3,2,4,5]
c=[]
for i in a:
    c.append(i*i)
print(c)
for i in b:
    c.append(i*i)
print(c)
for i in d:
    c.append(i*i)
print(d)





a=[4,5,6,7,4,3,2,3,5]
d=[7,5,6,7,88,3333,4,5]
f=[5,44,33,5,6,77,]
b=[]
c=[]
e=[]
for i in a:
    b.append(i*i)
print(b)
for i in d:
    c.append(i*i)
print(c)
for i in f:
    e.append(i*i)
print(e)







a=[12,2,3444,234,444,455666]
for i in a:
    if i==3444:
        b=a.index(i)
        #b.insert(i,20)
        a.insert(b,20)
        print(a)
        break
        #print(b)
        
        
        
        
        

a=[5,2,3,4,5,6,71,2,3,4]
a.sort()
print(a)
a.reverse()
print(a)


a=[5,5,6,7,4,3]
b=[4,5,6,7,7]
print(a+b)




a=[91,2,34,5,6,6,7,8]
b=[]
c=[6,7,7,5,4,3,3,4,5,5]
d=[]
e=list((9,8,7,6,5,98))
f=[]
for i in a:
    b.append(i*i)
print(b)
for i in c:
    d.append(i*i)
print(c)
for i in e:
    f.append(i*i)
print(f)

'''
a=[5,6,7,8,9,0,1,]
b=[]
c=[5,6,7,8,9,0,111,2,3]
d=[]
b=a.copy()
print(b)
d=c.copy()
print(d)
b.append(a)
print(b)
d=c.copy()
print(d)

a=[3,4,5,6,7,8,2,3,4,6]
a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)



#in the place of (first)5 we have to add 200
a=[3,4,5,6,7,8,2,3,4,6,5]
for i in a:
    if i==5:
        b=a.index(i)
        a.insert(b,200)
        print(a)
        break



a=[66,77,88,99,22,11,0,33,44,55,66,7,8,9,0]
a.sort()
print(a)
print(a.index(0))
a.reverse()
print(a)
for i in a:
    if i==0:
        b=a.index(i)
        a.insert(b,10000)
        print(a)
        break





























































































































































