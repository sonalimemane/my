'''

#anagram
a=input("Enter string 1:")

b=input("Enter string 2:")

count=0

for i in a:

    for j in b:

        if i==j:

            count=count+1

if count==len(a):
    print( It is anagram)

else:
    
    print("Strings are not anagram of each other.")

   

#isogram
x=input("enter the word")
count=0
      for i in x:
 count += x.count(i)
 
if count == len(x):
  print('It is isogram')
else:
  print('It not isogram')


'''
#pangram
n=input("Enter string 1:")

#string="The quick brown fox jumps over the lazy dog hgkhklk"
alphabet="abcdefghijklmnopqrstuvwxyz"
c=0
for i in alphabet:
    if i not in n:
        c=1
if c==0:
    print("It is Pangram")
else:
    print("It Not pangram")
