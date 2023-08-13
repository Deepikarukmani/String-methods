#print forward direction with different methods:
s = 'Today is sunday'
for i in s:
    print(i , end=" ")

#print forward direction with different methods:
s = 'Today is sunday'
for i in range(len(s)):
    print(s[i] , end=" ")

#print forward direction with different methods:
s = 'Today is sunday'
for i in s[::]:
    print(i, end=" ")


#print backward direction with different methods:
s = 'Today is sunday'
for i in s[::-1]:
    print(i, end=" ")

#print backward direction with different methods:
s = 'Today is sunday'
l= len(s)
for i in range(l -1, -1, -1,):
    print(s[i], end=" ")

#print backward direction with different methods:
s = 'Today is sunday'
l= len(s) - 1
while l>=0:
    print(s[l], end=" ")
    l-=1

#membership operator:
name= "deepika"
print('i' in name)
print('i' not in name)


#membership operator:
sen = input("Enter any sentence")
word = input("enter any word to search")
if word in sen:
    print("word is present")
else:
    print("word is not present")


#membership operator:
s1 = input("enter any word")
s2 = input("enter any word")
if s1==s2:
    print("s1 snd s2 sre equal")
elif s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")