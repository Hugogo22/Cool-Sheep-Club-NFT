import random
import os
from PIL import Image
from time import perf_counter
from math import exp, trunc

nbtest = [0] * 8

alreadyGenerated = set()

dirlist = os.listdir(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB"))
imglist = []
selection = [0] * 15
probability = [1] * 10000
selectionnum = [[0] * 15] * 10000
temp = [0] * 10
p = [
    #background 0
    [0.08, 0.07, 0.07, 0.07, 0.07, 0.02, 0.07, 0.05, 0.08, 0.04, 0.1, 0.08, 0.05, 0.07, 0.07, 0.01],
    #fur 1
    [0.005, 0.05, 0.08, 0.09, 0.01, 0.065, 0.018, 0.025, 0.06, 0.012, 0.005, 0.075, 0.02, 0.035, 0.025, 0.01, 0.015, 0.012, 0.011, 0.04, 0.04, 0.029, 0.02, 0.045, 0.04, 0.055, 0.013, 0.01, 0.01, 0.035, 0.02, 0.02],
    #vetement 2
    [0.02, 0.206, 0.05, 0.075, 0.035, 0.038, 0.065, 0.05, 0.048, 0.046, 0.025, 0.07, 0.272],
    #mouths 3
    [0.17, 0.13, 0.12, 0.1, 0.13, 0.09, 0.11, 0.08, 0.07],
    #eyes 4 
    [0.11, 0.08, 0.01, 0.05, 0.075, 0.04, 0.035, 0.03, 0.045, 0.06, 0.07, 0.09, 0.08, 0.07, 0.07, 0.05, 0.035],
    #earrings 6 5
    [0.2, 0.2, 0.15, 0.2, 0.25],
    #cheveux 7 6
    [0.22, 0.045, 0.06, 0.175, 0.135, 0.025, 0.13, 0.08, 0.05, 0.08],
    #chapo 8 7
    [0.1, 0.1, 0.08, 0.08, 0.06, 0.08, 0.06, 0.1, 0.1, 0.24],
    #accessoires 5 8
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #accessoires 52 9
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.12, 0.27],
    #accessoires 53 10
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #accessoires 54 11
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #accessoires 55 12
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #accessoires 56 13
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #accessoires 57 14
    [0.135, 0.03, 0.06, 0.09, 0.09, 0.135, 0.08, 0.044, 0.066, 0.27],
    #chapo 82 15
    [0, 0, 0, 0, 0.06, 0, 0, 0, 0.1, 0.84],
    #nb accessoires 16
    [0.6, 0.2, 0.1, 0.06, 0.03, 0.0097, 0.004]
]
#Counts the number of times an accessory was selected
#attrCount = [[0] for i in range(len(p[i]))] * 9

t1 = perf_counter()

nbGen = int(input("How many nfts do you want to generate ? "))

#--- Image Generation ---

for dir in dirlist:
    imglist.append(os.listdir(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + dir)))
    
random.seed()
try:
    os.mkdir(os.path.join(os.path.dirname(__file__), "IMAGES"))
except FileExistsError:
    None
try:
    os.mkdir(os.path.join(os.path.dirname(__file__), "temp"))
except FileExistsError:
    None
file = open(os.path.join(os.path.dirname(__file__), "temp/parts.txt"), "w")
for gen in range(1, nbGen + 1):
    i = gen-1

    if (i%500 == 0):
        print(str(i) + " done ...")
    
    #Random parts generation

    notverified = True
    while notverified:
        for j in range(7):
            selectionnum[i][j] = random.choices( range(len(imglist[j])), p[j])[0]
            selection[j] = imglist[j][selectionnum[i][j]]
            probability[i] *= p[j][selectionnum[i][j]]

        if (selection[6] == "cheveux 9_Afro.png"):
            selectionnum[i][7] = random.choices( range(len(imglist[7])), p[15])[0]
            selection[7] = imglist[7][selectionnum[i][7]]
            probability[i] *= p[7][selectionnum[i][7]]
        else:
            selectionnum[i][7] = random.choices( range(len(imglist[7])), p[7])[0]
            selection[7] = imglist[7][selectionnum[i][7]]
            probability[i] *= p[7][selectionnum[i][7]]
            

        #Random accessory generation
        #In temp accessories that have already been chosen have a probability of 0
        for j in range(len(temp)-1):
            temp[j] = p[9][j]
        
        TatooNotFirst = False
        
        nbAccessories = random.choices(range(1, 8), p[16])[0]
        for k in range(nbAccessories):
            
            #The tatoo accessory can only be on the first layer
            if k == 1:
                if temp[8] != 0:
                    temp[8] = 0
                    TatooNotFirst = True
            #If there is no tatoo the nft can't have more than 6 accessories
            if k == 6 and TatooNotFirst == True:
                nbAccessories = 6
                break
            selectionnum[i][8 + k] = random.choices( range(len(imglist[9])), temp)[0]
            probability[i] *= temp[selectionnum[i][8+k]]
            temp[selectionnum[i][8 + k]] = 0
            selection[8 + k] = imglist[9][selectionnum[i][8 + k]]
            if (selectionnum[i][8 + k] == 5 or selectionnum[i][8 + k] == 6 or selectionnum[i][8 + k] == 7):
                temp[5]= 0
                temp[6]= 0
                temp[7]= 0
            #print(k,":", temp, ":", selectionnum)
        
        for m in range(nbAccessories, 7):
            selectionnum[i][8 + m] = -1
            selection[8 + m] = imglist[9][9]

        nbtest[nbAccessories]+=1

        #nft 314 is rigged
        if i == 314:
            selectionnum[314][0] = 15
            selection[0] = "BGa16 - _Galactic.png"
            selectionnum[314][1] = 15
            selection[1] = "FURa11 - _Galactic.png"
            selectionnum[314][2] = -1
            selection[2] = "w_WOUAH C VIDE.png"
            selectionnum[314][6] = 5
            selection[6] = "CHEVEUX 6_Galactic.png"

        actual = "".join(x for x in selection)
        if actual in alreadyGenerated:
            print("Double! New generation ...")
        else:
            notverified = False
            alreadyGenerated.add(actual)

    #print(selection)
    
    #Adding folder to path
    for s in range(len(selection)):
        selection[s] = dirlist[s] + "/" + selection[s]

    #Temp file writing for metadata generation
    for x in selection:
        file.write(x + ",")
    file.write("\n")
    
    #Image creation

    nimage = Image.new("RGBA", (720, 720))

    for v in range(3):
        im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + selection[v]))
        nimage.alpha_composite(im)

    im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB_BASE/1LIGHTS AND SHADOWS.png"))
    nimage.alpha_composite(im)

    im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB_BASE/2CONTOURS.png"))
    nimage.alpha_composite(im)

    
    im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + selection[4]))
    nimage.alpha_composite(im)
    
    for v in range(8, 8 + nbAccessories):
        im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + selection[v]))
        nimage.alpha_composite(im)

    im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + selection[3]))
    nimage.alpha_composite(im)

    for v in range(5, 8):
        im = Image.open(os.path.join(os.path.dirname(__file__), "COOL_SHEEP_CLUB/" + selection[v]))
        nimage.alpha_composite(im)

    nimage = nimage.convert("RGB")
    nimage.save(os.path.join(os.path.dirname(__file__), "IMAGES/" + str(gen)), "PNG")

print(nbtest)
file.close()


#--- Price Generation ---

print("Generating prices ...")
pricesFile = open(os.path.join(os.path.dirname(__file__), "prices.txt"), "w")
min = 1
max = 0
for i in range(1, nbGen + 1):
    if (min > probability[i-1]):
        min = probability[i-1]
    if (max < probability[i-1]):
        max = probability[i-1]
    #probability[i] = 1 / (1 + exp(probability[i]))

for i in range(1, nbGen + 1):
    probability[i-1] = exp((probability[i-1] - min)*100000000)*0.005
    pricesFile.write(str(i) + " : " + str(probability[i-1]) + "\n")

pricesFile.close()

t2 = perf_counter()
print(t2-t1)