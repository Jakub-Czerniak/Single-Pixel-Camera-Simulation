from PIL import Image
import sys
import numpy as np
from matplotlib import pyplot as plt

class SinglePixelCamera:
    def __init__(self, image, samplePercent):
        if(image.size[0]==image.size[1]):
            self.imageSize = image.size[0]
            self.sampleCount = int(self.imageSize ** 2 * samplePercent / 100)
            self.values = np.empty(self.sampleCount)
            self.mask = np.zeros((self.imageSize**2,self.imageSize**2))
            self.image = np.asarray(image)
        else:
            sys.exit("Height and width of image does not match.")

    def PlotOriginal(self):
        plt.figure()
        plt.imshow(self.image, cmap='gray')
        plt.colorbar()
        plt.suptitle('Original image')
        plt.show()

    def CreateHadamardMask(self):
        px = self.imageSize**2
        self.mask = np.zeros((px,px))
        self.mask[0][0] = 1
        p = 1
        while(p<px):
            for i in range(p):
                for j in range(p):
                    if(i+p<px):
                        self.mask[i+p][j]=self.mask[i][j]
                    if(j+p<px):
                        self.mask[i][j+p]=self.mask[i][j]
                    if(j+p<px and i+p<px):
                        self.mask[i+p][j+p]=-self.mask[i][j]
            p*=2

    def CreateRandomMask(self):
        self.CreateHadamardMask()
        np.random.shuffle(self.mask)

    def PlotMask(self):
        plt.figure()
        plt.imshow(self.mask, cmap='gray')
        plt.colorbar()
        plt.suptitle('Mask')
        plt.show()

    def Aqusition(self):
        for i in range(self.sampleCount):
            maskPlus = (self.mask[i]+1)/2
            maskMinus = (1-self.mask[i])/2
            plusValue = maskPlus @ self.image.flatten()
            minusValue = maskMinus @ self.image.flatten()
            self.values[i] = plusValue - minusValue

    def AddNoise(self):
        sys.exit("Not implemented")

    def Recover(self):
        self.recovered = np.empty(self.imageSize**2)
        for j in range(self.sampleCount):
            self.recovered += self.mask[j] * self.values[j] / self.imageSize**2
        self.recovered = self.recovered.reshape(self.imageSize,self.imageSize)

    def PlotRecovered(self):
        plt.figure()
        plt.imshow(self.recovered, cmap='gray')
        plt.colorbar()
        plt.suptitle('Recovered image')
        plt.show()
 
    
image = Image.open("images\photos\cameraman.tif")
image = image.convert('L')
image = image.resize((128,128))
spc = SinglePixelCamera(image=image, samplePercent=20)
spc.CreateRandomMask()
spc.PlotMask()
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()