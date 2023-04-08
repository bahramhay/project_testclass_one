import functions
import re
materialsDict={}
cookiesDict={}

numberOfMaterials=input("number of materials: \n")
for x in range(int(numberOfMaterials)):
    inputed = input("material: \n")
    words=inputed.split()
    if words[0]=="add":
        functions.adding_materials(materialsDict,words[1],words[2])
print(materialsDict)

numberOfCookies=input("number of cookies: \n")
for x in range(int(numberOfCookies)):
    inputed = input("cookie: \n")
    new_inputed=re.sub(":"," ",inputed)
    new_inputed=re.sub(","," ",new_inputed)
    words=new_inputed.split()
    # print(words)
    # print(new_inputed, len(words))
    number_of_elements_per_cookie = int((len(words)-4)/2)
    if (words[0]=="define" and words[1]=="suit"):
        functions.defining_cookies(cookiesDict,words[2],words[3],number_of_elements_per_cookie,words)
print(cookiesDict)
