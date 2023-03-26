import sys
from PIL import Image

class SinglePixelCamera:
    __image = Image.new()

    def Aqusition(self, image, sampleCount, mode):
        if(mode=="Hadamard"):
            print("Hadamard")
        elif(mode=="Random"):
            print("Random")
        else:
            print("Error: Avaible modes: Hadamard, Random")
            sys.Exit()

    def AddNoise(self):
        print("Not implemented")
        sys.Exit()

    def Recovery(self):
        print("Not implemented")
        sys.Exit()

    def PlotImage():
        print("Not implemented")
        sys.Exit()