def countc(text ,char):
    dic = {}
    cc = 1
    for i in text:
        dic[i] = cc
        if i in char:
            cc +=1


    return dic[char]


text = input()
char = input()
result = countc(text,char)
print(result)