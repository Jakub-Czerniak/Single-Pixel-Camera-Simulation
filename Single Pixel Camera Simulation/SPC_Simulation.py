from PIL import Image
import sys
import numpy as np


def Aqusition(image, samplePercent, mode):
    if(image.size[0]==image.size[1]):
        px = int(image.size[0] * samplePercent / 100)
    else:
        print("Height and width of image does not match.")
        sys.Exit()
    image = image.resize((px,px))
    if(mode=="Hadamard"):
        hadamard = MakeHadamard(px)
        hadamardPlus = (hadamard+1)/2
        hadamardMinus = (1-hadamard)/2
        print (hadamardMinus)
        print (hadamardPlus)

    elif(mode=="Random"):
        print("Random")
    else:
        print("Error: Avaible modes: Hadamard, Random")
        sys.Exit()


def AddNoise():
    print("Not implemented")
    sys.Exit()


def Recovery():
    print("Not implemented")
    sys.Exit()


def PlotImage():
    print("Not implemented")
    sys.Exit()

def MakeHadamard(px):
    hadamard = np.zeros((px,px))
    hadamard[0][0] = 1 
    p = 1
    while(p<px):
        for i in range(p):
            for j in range(p):
                if(i+p<px):
                    hadamard[i+p][j]=hadamard[i][j]
                if(j+p<px):
                    hadamard[i][j+p]=hadamard[i][j]
                if(j+p<px and i+p<px):
                    hadamard[i+p][j+p]=-hadamard[i][p]
        p*=2
    return hadamard

image = Image.open("images\photos\Kansas-City.png")
Aqusition(image=image, samplePercent=10, mode="Hadamard")


#SinglePixelCamera.Recovery()
#SinglePixelCamera.PlotImage()