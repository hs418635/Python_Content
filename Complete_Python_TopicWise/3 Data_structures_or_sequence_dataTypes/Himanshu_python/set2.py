#set

'''1.duplication not allowed
2.random variable

3.can do mathemetical operation
intersection
union
difference
symmetrical_difference
updation
deletion
4.not indexed'''


s={1,2,3,4,5}
#print(type(s))
#s1=set()
#print(type(s1))
#print(s.add(10))
print(s.update([11,23,45]))
#s.discard(11)
#print("after discarding",s)
s.remove(45)
print("after removing",s)

#discard---remove

#two sets
s1={1,2,3}
s2={2,3,4}
s1.union(s2)
s1.difference(s2)
s2.difference(s1)
s.intersection(s1)

for i in s:
	print(i)


	
#################################################################
"""1. unordered collection
2.accssed by keys not by index
3.variable length add/del
4.immutable (can't change)"""

d={}
type(d)
#syntax:d={keys:values}

d={a:"python" ,b:"django",c:"AI",d:"DS"}
print(d)

#inbuit dictionary
d1=dict(name="Amar",Age="24")
d1['name']
d1['Age']

d1.get('Age')#24
d1.values()#Amar,24
d1.keys()#name,age
d1.popitem()#age=24
d2=d1.copy()#name='amar'
d1.items()#all pairs of keys & values

      
