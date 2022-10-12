Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='wertyuio'
b="wertyuio"
c=''' giya bichwalia'''
print(c)
 giya bichwalia
hello worlds'
SyntaxError: unterminated string literal (detected at line 1)
a[0]
'w'
a[6]
'i'
a[-1]
'o'
print(c[0:2])
 g
a="hello"
a[starting point:stop:step]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a[0:2]
'he'
a[-1:-3:-1]
'ol'
a[4:6]
'o'
a[3:6]
'lo'
a[:11:2]
'hlo'
#dlrow olleh
a[-1::-1]
'olleh'
a[::-1]
'olleh'
a[-3:0]
''
a='hello world'
a.capitalize()
'Hello world'
a
'hello world'
a=a.capitalize()
a
'Hello world'
a='hello world'
a.title()
'Hello World'
a.center(50)
'                   hello world                    '
a.center(50,'#')
'###################hello world####################'
a.count('1'
        a.count('1')
        
SyntaxError: '(' was never closed
a.count('1')
        
0
a.count('e')
        
1
a.lstrip()
        
'hello world'
a.rstrip()
        
'hello world'
a.islower()
        
True
a.upper()
        
'HELLO WORLD'
a.lower()
        
'hello world'
a.startswith('he')
        
True
len(a)
        
11
11
        
11
a[0]='m'
        
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a[0]='m'
TypeError: 'str' object does not support item assignment
del[a]
        
b='akshat123@gmail.com'
        
b.split('@')
        
['akshat123', 'gmail.com']
'@'.join(b)
        
'a@k@s@h@a@t@1@2@3@@@g@m@a@i@l@.@c@o@m'
m=[12,'hi',2.3,500]
        
m=[0]
        
m=[12,'hi',2.3,500]
        
m[0]
        
12
m[1:3]
        
['hi', 2.3]
'hi' in m
        
True
'hello'in m
        
False
'hi' not in m
        
False
2*m
        
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
4*m
        
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
m+=['new value']
        
m +=['new value']
        
m
        
[12, 'hi', 2.3, 500, 'new value', 'new value']
m.append('abc')
        
m
        
[12, 'hi', 2.3, 500, 'new value', 'new value', 'abc']
m.extend(['x','y','kuch bhi'])
        
m
        
[12, 'hi', 2.3, 500, 'new value', 'new value', 'abc', 'x', 'y', 'kuch bhi']
a.insert92,'hello')
SyntaxError: unmatched ')'
m.insert(2,'hello')
m.insert(2,'hello')
m
[12, 'hi', 'hello', 'hello', 2.3, 500, 'new value', 'new value', 'abc', 'x', 'y', 'kuch bhi']
m.pop()
'kuch bhi'
mp = m.pop()
mp
'y'
m
[12, 'hi', 'hello', 'hello', 2.3, 500, 'new value', 'new value', 'abc', 'x']
m.clear()
m
[]
n=[0,8,7,6]
n.reverse()
n
[6, 7, 8, 0]
n.sort()
n
[0, 6, 7, 8]
max(n)
8
min(n)
0
m=[12,'hi',2.3,500,'new value']
m.index('hi')
1
m[1][0]
'h'
####################################################
t=52,23,'abc'
type(t)
<class 'tuple'>
len(t)
3
t.index('abc')
2
t[0]
52
t[:2]
(52, 23)
t[0]
52
t
(52, 23, 'abc')
k =(12,52,85,(5,'abc',5.5),100)
type(t)
<class 'tuple'>
type(k)
<class 'tuple'>
k[3]
(5, 'abc', 5.5)
k[3][1]
'abc'
k[3][1][1]
'b'
t
(52, 23, 'abc')
##############################
s = {1,1,2,2,3,4,4,3}
type(s)
<class 'set'>
print (s)
{1, 2, 3, 4}
s
{1, 2, 3, 4}
s[0:2]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s[0:2]
TypeError: 'set' object is not subscriptable
s2={23,3,41,4}
s.intersection(s2)
{3, 4}
s.union(s2)
{1, 2, 3, 4, 41, 23}
s.add(100)
s
{1, 2, 3, 100, 4}
s.discard(100)
s
{1, 2, 3, 4}
s.remove(3)
s
{1, 2, 4}
s1={44,22,33]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s1 = {44,22,33}
s.update(s1)
s
{1, 2, 33, 4, 44, 22}
s.clear()
s
set()
