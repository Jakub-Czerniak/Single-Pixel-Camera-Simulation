from PIL import Image
import sys
import numpy as np
from matplotlib import pyplot as plt


def Aqusition(image, samplePercent, mode):
    if(image.size[0]==image.size[1]):
        imageSize = image.size[0]
        sampleCount = int(imageSize ** 2 * samplePercent / 100)
    else:
        print("Height and width of image does not match.")
        sys.Exit()
    image = np.asarray(image)
    if(mode=="Hadamard"):
        hadamard = MakeHadamard(imageSize**2)
        plt.figure()
        plt.imshow(hadamard)
        plt.colorbar()
        plt.show()
        #print("image")
        #print(image)
        values = np.empty(sampleCount)
        for i in range(sampleCount):
            maskPlus = (hadamard[i]+1)/2
            maskMinus = (1-hadamard[i])/2
            #print(maskPlus)
            #print(maskMinus)
            plusValue = maskPlus @ image.flatten()
            minusValue = maskMinus @ image.flatten()
            #print("Plus value: " + str(plusValue))
            #print("Minus value: " + str(minusValue))
            values[i] = plusValue - minusValue
            #print(values)
        print(values)
        #recover = np.linalg.solve(hadamard[0:sampleCount],values)
        recover = np.empty(imageSize**2)
        for j in range(sampleCount):
            print(hadamard[j])
            print(values[j])
            recover += hadamard[j] * values[j]
            print(recover)
        recover = recover.reshape(imageSize,imageSize)

        plt.figure()
        plt.imshow(recover)
        plt.colorbar()
        plt.show()
        print(recover)

    elif(mode=="Random"):
        sys.Exit()
        #random = MakeRandomMatrix(px, image.size[0])
    else:
        print("Error: Avaible modes: Hadamard, Random")
        sys.Exit()


def AddNoise(matrix):
    print("Not implemented")
    sys.Exit()


def Recovery(values):
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
                    hadamard[i+p][j+p]=-hadamard[i][j]
        p*=2
    return hadamard

def MakeRandomMatrix(px, size):
    for i in range(px):
        randomV = np.random.random(size)
 
    
image = Image.open("images\photos\sample_256pixel.png")
image = image.convert('L')

Aqusition(image=image, samplePercent=100, mode="Hadamard")

#SinglePixelCamera.Recovery()
#SinglePixelCamera.PlotImage()