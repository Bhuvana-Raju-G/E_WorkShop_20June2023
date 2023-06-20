import pyttsx3
from PIL import Image

def Image_Size(Image,width,height):
    print(Image," image width is ",width,"height is ",height)
    engine.say(Image+" image ,")
    engine.say("width is")
    engine.say(width)
    engine.say("Height is ")
    engine.say(height)
    engine.runAndWait()
    
    
#Initialzing the engine
engine=pyttsx3.init()

#Image Object
im=Image.open("Codes/leaf.jpg")


#Size of original Image
width=im.width
height=im.height
Image="Original"
Image_Size(Image,width,height)



