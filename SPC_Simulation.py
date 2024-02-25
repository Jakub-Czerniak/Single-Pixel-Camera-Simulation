from PIL import Image
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure

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

    def CreateCakeCuttingMask(self):
        self.CreateHadamardMask()
        numberOfConnected = np.zeros(self.imageSize**2)
        for rowNumber, row in enumerate(self.mask):
            matrix = row.reshape(self.imageSize,self.imageSize)
            numberOfConnected[rowNumber]= measure.label(label_image=matrix, return_num=True, connectivity=1)[1]
        indices = np.argsort(numberOfConnected)
        self.mask = self.mask.take(indices, 0)

    def CreateWalshMask(self):
        self.CreateHadamardMask()
        numberOfConnected = np.zeros(self.imageSize**2)
        for rowNumber, row in enumerate(self.mask):
            numberOfConnected[rowNumber]= measure.label(label_image=row, return_num=True, connectivity=1)[1]
        indices = np.argsort(numberOfConnected)
        self.mask = self.mask.take(indices, 0)

    def CreateHighFrequencyMask(self):
        self.CreateHadamardMask()
        numberOfConnected = np.zeros(self.imageSize**2)
        for rowNumber, row in enumerate(self.mask):
            numberOfConnected[rowNumber]= measure.label(label_image=row, return_num=True, connectivity=1)[1]
        indices = np.argsort(numberOfConnected)
        self.mask = self.mask.take(indices[::-1], 0)

    def SaveMaskToFile(self, file):
        with open(file=file, mode='wb+') as f:
            np.save(f, self.mask)

    def ReadMaskFromFile(self, file):
        with open(file=file, mode='rb') as f:
            self.mask=np.load(file=f)

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

    def SaveRecovered(self, file_name='recovered.tif'):
        Image.fromarray(normalization_grayscale(self.recovered)).convert('L').save(file_name)


def normalization_grayscale(image):
    img_max = image.max()
    img_min = image.min()
    if img_min < 0:
        image += abs(img_min)
    if not img_max == 255 and img_min == 0:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i][j] = 255 * (image[i][j] - img_min) / (img_max - img_min)
    return image.astype(np.uint8)


if not os.path.exists('masks/'):
    os.makedirs('masks/')
if not os.path.exists('recovered/'):
    os.makedirs('recovered/')

image = Image.open('photos/lena_gray_256.tif')
image = image.convert('L')
image = image.resize((128,128))
spc = SinglePixelCamera(image=image, samplePercent=30)
spc.CreateHighFrequencyMask()
spc.SaveMaskToFile(file='masks/HighFrequency128.npy')
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()
spc.SaveRecovered('recovered/HighFreq30_128.tif')

spc.CreateHadamardMask()
spc.SaveMaskToFile(file='masks/Hadamard128.npy')
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()
spc.SaveRecovered('recovered/Hadamard30_128.tif')

spc.CreateRandomMask()
spc.SaveMaskToFile(file='masks/Random128.npy')
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()
spc.SaveRecovered('recovered/Random30_128.tif')

spc.CreateWalshMask()
spc.SaveMaskToFile(file='masks/Walsh128.npy')
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()
spc.SaveRecovered('recovered/Walsh30_128.tif')

spc.CreateCakeCuttingMask()
spc.SaveMaskToFile(file='masks/CakeCutting128.npy')
spc.Aqusition()
spc.PlotOriginal()
spc.Recover()
spc.PlotRecovered()
spc.SaveRecovered('recovered/CakeCutting30_128.tif')
