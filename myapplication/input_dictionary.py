import functions

materialsDict={}
numberOfMaterials=input("number of materials: \n")
for x in range(int(numberOfMaterials)):
    inputed = input("material: \n")
    words=inputed.split()
    if words[0]=="add":
        functions.adding_materials(materialsDict,words[1],words[2])
print(materialsDict)

