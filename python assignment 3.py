#!/usr/bin/env python
# coding: utf-8

# # python assignment 3

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# In[6]:


def myreduce(num):
    
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements
 
print("Input:")
number=int(input("Please insert the number :"))


output_value=myreduce(number)

print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])


# 1.2 Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

# In[25]:


letters = ["w","J","r","a","u","e","a","t","f","i","n","v","o","q","u","k","p",]

def filter_non_vowels(letters):
    vowels = ["a","e","i","o","u"]

    if(letters in vowels):
        return False
    else:
        return True 

filter_non_vowels = filter(filter_non_vowels, letters)

print("The filtered non-vowels are:")
for non_vowel in filter_non_vowels:
    print(non_vowel)


# 2 . Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# 
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[22]:



h_letters = []

for letter in "ACADGILD":
    h_letters.append(letter)

print(h_letters)

word_1=list("xyz")
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)

