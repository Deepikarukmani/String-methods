#formatting strings:

sen = "sunday is not holiday. he is not partner. it is not team"
print(id(sen))
sen = (sen.replace("not", "our",1))
print(id(sen))
print(sen)


sen = "sunday is not holiday. he is not partner. it is not team"
position = sen.rfind("not")
sen2 = sen[:position]
print(sen[:position:position+3])
print(sen[:position], "our", sen[position+4:])

#formatting strings:

sentence = "sunday is not holiday. he is not partner. it is not team"
alpha = "not"
index = -1
length = len(sentence)
count = 0

while not count == 2:
    index = sentence.find(alpha, index+1, length)
    if index == -1:
        print("Searched alphabet is not found")
        break
    print("Searched alphabet is present at ", index)
    count+=1
    #index+=1
else:
    print(sentence[:index], "our", sentence[index+4:])
