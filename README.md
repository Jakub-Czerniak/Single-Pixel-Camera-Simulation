Simulation of single pixel camera  
  
Masks - base masks are n^2 size of an image, each row is used as mask for image acquisition. Mask detemines which parts of orginal image are adding intesity to the sample (1 - white pixels) and which are substarcting (-1 - black pixels). Mask are differentiated by row sorting method and all are based on Hadamard mask.  
Example masks for 4x4 images:  
Hadamard masks:
![HADA](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/b9352a32-a272-4150-a1c7-8eef3b43b8f7)
Walsh masks:
![WALSH](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/63241d25-34a4-43e8-a0fe-03d6aed72dc0)
High frequncy masks:
![HIGHFREQ](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/14adcb6b-fb96-4743-9478-31681adfb5d4)
CakeCutting masks:
![CAKE](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/e80d0bb1-dbe4-4dd9-add1-c056f3bd0bb6)
Random masks:
![RANODM](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/ec7ccfda-1aec-4934-b4a4-225989b9f6f2)  
  
Images are sampled with sample percentage. At 30% image of size 128x128 is sampled 128 x 128 x 0.3 = 4915 times, using 4915 rows of base mask. Then from collected intensities image can be recovered.  
  
Orginal image:   
![orginal](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/157f5c1e-0791-4b13-b56b-ee3a8c568069)  
  
Images recovered with sample percentage = 30%.  
Hadamard masks:
![Hadamard30_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/8f8582f2-560f-4ee7-8060-a2d0bfd26a57)
Walsh masks:
![Walsh30_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/91d3e391-596f-4340-bba3-a76eaec960e8)
High frequncy masks:
![HighFreq30_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/e708771c-44bb-43b8-af26-d77b97e9a29f)
CakeCutting masks:
![CakeCutting30_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/a08e96bc-ebd5-4855-92e5-953f43b9cce2)
Random masks:
![Random30_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/0cb5d53a-1e14-4e62-8489-a62ba19f5977)
  
Images recovered with sample percentage = 50%.  
Hadamard masks:
![Hadamard50_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/04ce021a-6464-4152-a0d4-53661cc94409)
Walsh masks:
![Walsh50_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/10b41769-e8ca-49c3-b48f-e04e4944fdd9)
High frequncy masks:
![HighFreq50_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/f7cc5650-e196-4634-83af-0a40146c3209)
CakeCutting masks:
![CakeCutting50_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/d9b566fe-411c-44f5-a68d-94b761c53c0e)
Random masks:
![Random50_128](https://github.com/Jakub-Czerniak/Single-Pixel-Camera-Simulation/assets/62241802/6ef7ba4b-aa12-48ac-b260-305792fdd300)
