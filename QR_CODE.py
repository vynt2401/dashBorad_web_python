import qrcode

def generateByDefault(link):
    qrCode = qrcode.make(link)
    qrCode.save("qrcode.png")

