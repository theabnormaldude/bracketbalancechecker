# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:36:29 2019

@author: Shiv
"""
'''
num=int(input("Enter the number of brackets to check"))
brackets=["(",")","[","]","{","}"]

emp=[]

for i in range(num):
    user=input("Enter the brackets")
    emp.append(user)
    
print(emp)

print(list("shiv"))
'''

brack=input("Enter the brackets to check")
ls=list(brack)
count=0
#print(ls)
size=len(ls)
#print(size)
for i in range(size//2):
    #if(ls[i]==ls[size-i-1]):
    if(ord(ls[i])==40 and ord(ls[size-i-1])==41): 
#or (123 and 125))):
        count+=1
    elif(ord(ls[i])==91 and ord(ls[size-i-1])==93): 
        count+=1
    elif(ord(ls[i])==123 and ord(ls[size-i-1])==125): 
        count+=1
#print(count)

if count==size//2:
    print("Brackets are Balanced")
else:
    print("Brackets are Unbalanced")
    
    
    
    
    
    

stack=[]
brack=input("Enter the brackets to check")
bracket=list(brack)
length=len(brack)
def peek_stack(stack):
    if stack == []:
        return None
    else:
        return stack[-1]
for i in range(length):
    if (ord(bracket[i])==40 or ord(brack[i])==91 or ord(brack[i])==123):
        stack.append(bracket[i])
    elif (ord(bracket[i])==41):
        top=peek_stack(stack)
        if(ord(top)==40):
            stack.pop()
    elif (ord(bracket[i])==93):
        top=peek_stack(stack)
        if(ord(top)==91):
            stack.pop()
    elif (ord(bracket[i])==125):
        top=peek_stack(stack)
        if(ord(top)==123):
            stack.pop()
if len(stack)==0:
    print("Balanced String")
else:
    print("Unbalanced String")
            
        