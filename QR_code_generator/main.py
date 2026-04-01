# python qrcode documentation(for more knowledge)
import qrcode

url = input("Enter your url:")
filename = input("Filename you want to save it as:")

if(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)

# https://github.com/Kashishjangid05