import re

def adding_materials(dict,word1,word2):
    dict[word1]=int(word2)
    # print(dict)
    return(dict)

    # print(type(words[0]),type(words[1]),type(words[2]))
    # print(type(materialsDict[0][0]))

def defining_cookies(dict,word2,word3,numberOfElements,word):
    dict[word2]={}
    new_word3=re.sub(":","",word3)
    dict[word2]["price"]=int(new_word3)
    for x in range(numberOfElements):
        dict[word2][word[2*x+4]]=int(word[2*x+5])
    
    # print(dict)
    return(dict)