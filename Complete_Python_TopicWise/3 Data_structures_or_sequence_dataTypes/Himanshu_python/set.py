Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> type(s)
<class 'dict'>
>>> s={1,2}
>>> type(s)
<class 'set'>
>>> s={1,2,3}
>>> s1={2,5,6}
>>> s.add(120)
>>> s
{120, 1, 2, 3}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> for i in s:
	print(i)

	
120
1
2
3
>>> s.remove(1)
>>> s
{120, 2, 3}
>>> s.discrad(2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.discrad(2)
AttributeError: 'set' object has no attribute 'discrad'
>>> s.discard(2)
>>> s
{120, 3}
>>> s3={1,2,4}
>>> s3
{1, 2, 4}
>>> s1
{2, 5, 6}
>>> s1.update(s2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.update(s2)
NameError: name 's2' is not defined
>>> s1.update(s2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1.update(s2)
NameError: name 's2' is not defined
>>> s.update(s1)
>>> s
{2, 3, 5, 6, 120}
>>> s1
{2, 5, 6}
>>> s
{2, 3, 5, 6, 120}
>>> s1={1,2,3}
>>> s2={1,2,7}
>>> s1.difference(s2)
{3}
>>> s2.difference(s1)
{7}
>>> s1.symmetric_difference(s2)
{3, 7}
>>> s1.intersection(s2)
{1, 2}
>>> s1.union(s2)
{1, 2, 3, 7}
>>> 
