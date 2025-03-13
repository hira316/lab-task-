Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> academic_tuple =('name','father name','reg number','CNIC number','CGPA')
>>> Mr_A_registration =("FA24-BBA-078',)
		    
SyntaxError: EOL while scanning string literal
>>> Mr_A_registration =('FA24-BBA-078',)
>>> # A tuple of integers
>>> numbers_tuple =(1,2,3,4)
>>> # A tuple of strings
>>> fruit_tuple =('banana','cherry','orange')
>>> mixed_tuple =(1,'banana',3.78,True)
>>> single_item_tuple =(7,)
>>> print(fruit_tuple[1])
cherry
>>> print(fruit_tuple[-1])
orange
>>> print(fruit_tuple[0])
banana
>>> print(fruit_tuple[-2])
cherry
>>> tuple1 =(0,1,2,3)
>>> tuple2 =(4,5,6,7)
>>> combine_tuple =tuple1+tuple2
>>> print(combine_tuple)
(0, 1, 2, 3, 4, 5, 6, 7)
>>> tuple1 =('hira')
>>> repeated_tuple =tuple1*3
>>> print(repeated_tuple)
hirahirahira
>>> tuple1 =('hira',)
>>> repeated_tuple = tuple1 + 3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    repeated_tuple = tuple1 + 3
TypeError: can only concatenate tuple (not "int") to tuple
>>> repeated_tuple =tuple1*3
>>> print(repeated_tuple)
('hira', 'hira', 'hira')
>>>  tuple1 =('hira',)
>>> repeat_tuple = tuple1 + 3
SyntaxError: unexpected indent
>>> repeat =tuple1*3
>>> print(repeat)
SyntaxError: multiple statements found while compiling a single statement
>>> repeated_tuple =tuple1*3
>>> print(repeated_tuple)
SyntaxError: multiple statements found while compiling a single statement
>>> numbers =(1,2,3,4,5,6)
>>> print(numbers[0:2])
(1, 2)
>>> print(numbers[1:3])
(2, 3)
>>> print(numbers[:6])
(1, 2, 3, 4, 5, 6)
>>> fruit_tuple =('banana','orange','cherry')
>>> print(fruit_tuple.count('banana'))
1
>>> print(fruit.index('cherry'))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(fruit.index('cherry'))
NameError: name 'fruit' is not defined
>>> print(fruits.index('cherry'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(fruits.index('cherry'))
NameError: name 'fruits' is not defined
>>> print(fruits.index('orange'))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(fruits.index('orange'))
NameError: name 'fruits' is not defined
>>> print(fruit_tuple.index('orange'))
1
>>> sum =0
>>> for i in range(6):
	sum =sum + i
	print (sum)
	FOR LOOP
	
SyntaxError: invalid syntax
>>> FOR LOOP
SyntaxError: invalid syntax
>>> sum = 0
>>> for i in range(6):
	sum = sum + i
	print(sum)

	
0
1
3
6
10
15
>>> sum = 0
>>> for i in range (6):
	if i = 3:
		
SyntaxError: invalid syntax
>>> if sum = 3:
	
SyntaxError: invalid syntax
>>> if i=3:
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> if i 3:
	
SyntaxError: invalid syntax
>>> a = 0 for i in range(6):
	
SyntaxError: invalid syntax
>>> for i in range(6):
	if i = 3:
		
SyntaxError: invalid syntax
>>> if i ==3:
	Break
	print(i)

	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = 0
>>> for i in range(6):
	if i ==3:
		break
	print(i)

	
0
1
2
>>> sum = 0
>>> while(i < = 5):
	
SyntaxError: invalid syntax
>>> while(i<==5):
	
SyntaxError: invalid syntax
>>> while i < =5:
	
SyntaxError: invalid syntax
>>> 
