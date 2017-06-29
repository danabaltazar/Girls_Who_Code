from PIL import Image

#functions
def negative(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = 255 - red #find new values
    newGreen = 255 - green
    newBlue = 255 - blue

    p = (newRed,newGreen,newBlue)
    
    newPixelList.append(p)
    
def overexpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255
        
    newBlue = red*2
    if newBlue > 255:
        newBlue = 255
        
    newGreen = red*2
    if newGreen > 255:
        newGreen = 255
        
    p = (newRed,newGreen,newBlue)   
    
    newPixelList.append(p)

      
#running code
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
halfway = length//2

counter = 0

for pixel in pixelList:
    #pixel manipulation
    if (counter < halfway):#is top half of the photo
        overexpose(pixel)
        
    else:#this the bottom of half photo
        negative (pixel)  
    counter = counter + 1

newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()

    

