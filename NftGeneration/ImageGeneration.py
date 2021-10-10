import random
from os import listdir
from PIL import Image
from time import perf_counter

nbtest = [0] * 8

notnew = set()

dirlist = listdir("COOL_SHEEP_CLUB")
imglist = []
selection = [0] * 15
#selectionnum = [0] * 7
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
    [0.6, 0.2, 0.1, 0.06, 0.03, 0.0097, 0.0007]
]

t1 = perf_counter()

for dir in dirlist:
    imglist.append(listdir("COOL_SHEEP_CLUB/" + dir))
    
random.seed()
file = open("parts.txt", "w")
for i in range(1, int(input("Nombre de generations:")) + 1):

    notverified = True
    while notverified:
        for j in range(7):
            selection[j] = random.choices(imglist[j], p[j])[0]

        if (selection[6] == "cheveux 9_Afro.png"):
            selection[7] = random.choices(imglist[7], p[15])[0]
        else:
            selection[7] = random.choices(imglist[7], p[7])[0]
            

        for j in range(len(temp)-1):
            temp[j] = p[9][j]
        
        TatooNotFirst = False

        nbaccessoires = random.choices(range(1, 8), p[16])[0]
        for k in range(nbaccessoires):
            
            if k == 1:
                if temp[8] != 0:
                    temp[8] = 0
                    TatooNotFirst = True
            if k == 6 and TatooNotFirst == True:
                nbaccessoires = 6
                break
            selectionnum = random.choices( range(len(imglist[9])), temp)[0]
            temp[selectionnum] = 0
            selection[8 + k] = imglist[9][selectionnum]
            if (selectionnum == 5 or selectionnum == 6 or selectionnum == 7):
                temp[5]= 0
                temp[6]= 0
                temp[7]= 0
            #print(k,":", temp, ":", selectionnum)
        
        for m in range(nbaccessoires, 7):
            selection[8 + m] = imglist[9][9]

        nbtest[nbaccessoires]+=1

        if i == 314:
            selection[0] = "BGa16 - _Galactic.png"
            selection[1] = "FURa11 - _Galactic.png"
            selection[6] = "CHEVEUX 6_Galactic.png"
            selection[2] = "w_WOUAH C VIDE.png"
            selection[7] = "HALO_Halo.png"

        actual = "".join(x for x in selection)
        if actual in notnew:
            print("Not new")
        else:
            notverified = False
            notnew.add(actual)

    #print(selection)
    
    for s in range(len(selection)):
        selection[s] = dirlist[s] + "/" + selection[s]


    for x in selection:
        file.write(x + ",")
    file.write("\n")


    nimage = Image.new("RGBA", (720, 720))

    for v in range(3):
        im = Image.open("COOL_SHEEP_CLUB/" + selection[v])
        nimage.alpha_composite(im)

    im = Image.open("COOL_SHEEP_CLUB_BASE/1LIGHTS AND SHADOWS.png")
    nimage.alpha_composite(im)

    im = Image.open("COOL_SHEEP_CLUB_BASE/2CONTOURS.png")
    nimage.alpha_composite(im)

    
    im = Image.open("COOL_SHEEP_CLUB/" + selection[4])
    nimage.alpha_composite(im)
    
    for v in range(8, 8 + nbaccessoires):
        im = Image.open("COOL_SHEEP_CLUB/" + selection[v])
        nimage.alpha_composite(im)

    im = Image.open("COOL_SHEEP_CLUB/" + selection[3])
    nimage.alpha_composite(im)

    for v in range(5, 8):
        im = Image.open("COOL_SHEEP_CLUB/" + selection[v])
        nimage.alpha_composite(im)

    nimage = nimage.convert("RGB")
    #nimage = nimage.resize((400, 400), Image.LANCZOS)
    nimage.save("IMAGES/" + str(i) + ".png", "PNG")
    
    
file.close()
print(nbtest)

t2 = perf_counter()
print(t2-t1)