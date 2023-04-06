mydict={}
# mydict["shekar"]=10
inputed = input()
words=inputed.split()

if words[0]=="add":
    mydict[words[1]]=int(words[2])

print(mydict)
print(type(words[0]),type(words[1]),type(words[2]))
print(type(mydict[0][0]))
