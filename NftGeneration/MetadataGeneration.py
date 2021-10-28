from os import listdir
import json
from time import perf_counter

dirlist = listdir("COOL_SHEEP_CLUB")
imglist = []
names = [
    "Background",
    "Fur",
    "Clothes",
    "Mouth",
    "Eyes",
    "Earrings",
    "Hair",
    "Hat",
    "Accessory",
    "Accessory",
    "Accessory",
    "Accessory",
    "Accessory",
    "Accessory",
    "Accessory"
]
t1 = perf_counter()

baseURI = input("Input your nft images baseURI: ")

for dir in dirlist:
    imglist.append(listdir("COOL_SHEEP_CLUB/" + dir))

file = open("temp/parts.txt", "r")
count = 1
for line in file:
    jsonfile = open("METADATA/" + str(count), "w")
    metadata = {
        "image": baseURI + str(count),
        "attributes": []
    }
    selection = line.split(",")
    selection.pop()
    for i in range(len(selection)):
        selection[i] = selection[i].split("/")[1]
        selection[i] = selection[i].split(".")[0]
        selection[i] = selection[i].split("_")[1]
    for i in range(len(names)):
        if selection[i] != "WOUAH C VIDE":
            metadata["attributes"].append({
                "trait_type": names[i],
                "value": selection[i]
            })
    jsonfile.write(json.dumps(metadata))
    jsonfile.close()
    count += 1
file.close()
t2 = perf_counter()
print(t2-t1)