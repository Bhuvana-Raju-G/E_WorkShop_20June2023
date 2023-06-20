
from PIL import Image

#Accessing an Image
im=Image.open("codes/leaf.jpg")
#im.show()

#Image Details
print("image 1" ,im.width,im.height)


#Resizing an Image
im1=im.resize((3360,2240))
print("resized Image",im1.width,im1.height)
im1.save("newleaf.jpg")
#im1.show()

#Cropping an Image
im2=im.crop((400,400,1200,1200))
im2.save("cropped.jpg")
im2.show()
print("Cropped Image",im2.width,im2.height)