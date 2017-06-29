from PIL import Image

#Import the image
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

##    average = (red + green + blue) //3
##    
##
##    newRed = average
##    if newRed > 255:
##        newRed = 255
##
##
##        
##        
##    newGreen = average
##    if newGreen > 255:
##        newGreen = 255
##
##    newBlue = average
##    if newBlue > 255:
##        newBlue = 255
    newRed = 255 - red
    newGreen = 255 - green
    newBlue = 255 - blue
        


    p = (newRed,newGreen,newBlue)

    #add pixel to the new pixel list
    newPixelList.append(p)

    


#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
