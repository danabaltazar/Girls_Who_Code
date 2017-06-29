from PIL import Image

#functions

def redContrast(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newRed = red*2
    if newRed > 255:
        newRed = 255

    p = (newRed,green,blue)

    newPixelList.append(p)
    
def blackWhite(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    average = (red + green + blue) //3
    
    newRed = average
    if newRed > 255:
        newRed = 255
    
    newGreen = average
    if newGreen > 255:
        newGreen = 255

    newBlue = average
    if newBlue > 255:
        newBlue = 255
        
    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)
    
def blue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255

    p = (red,green,newBlue)

    newPixelList.append(p)

      
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
oneThird = length//3
twoThird = oneThird*2

counter = 0

for pixel in pixelList:
    #pixel manipulation
    if (counter < oneThird):#is top half of the photo
        redContrast(pixel)
    elif (counter < twoThird):
        blackWhite(pixel)
    else:#this the bottom of half photo
        blue (pixel)  
    counter = counter + 1

newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
