#space removal in a given string

sent = input("Enter any sentence")
print("before applying strip function")
print(sent, len(sent), "characters")
sent = sent.strip()
print("before applying strip function")
print(sent, "has", len(sent), "characters")


#to finding substrings:

name = "titikksha daughter of deepika and gowtham"

'''FIND''' #Find la oru illatha value ah search panna athu -1 nu result varum
#find la two types of find varum athu find and r find

print(len(name))
print(name.find("the")) # "the" is not in sentence so its output is -1
print(name.find("deepika",0,30))#first  la irunthu varum find na
print(name.find("titikksha"))

""" r find"""
print(name.rfind("and",0,30)) #reverse la irunthu varum rfind na
print(name.rfind("gowtham"))

""" INDEX""" #index la oru illatha value ah search panna athu value error nu kattum

print(name.index("the")) # "the" is not in sentence so its output is value error
print(name.index("deepika",0,30))
print(name.index("titikksha"))
print(name.index("gowtham"))


# ONE EXAMPLE PROGRAM to find the INDEX value:

name = input("what is your name? ")
alpha = input("enter any alphabet ")
index = 0

while True:
    index = name.find(alpha, index)
    if index == -1:
        print("Searched alphabet is not found")
        break
    print("Searched alphabet is present at index", index)
    index+=1


#buildin functions:

name = input("what is your name? ")
alpha = input("enter any alphabet ")
print(name.find(alpha,0,50))

print(name.index(alpha))

print(name.count(alpha,0,50))

print(name.count(alpha))

name = input("enter any sentence ")

print(name.replace("no", "now"))