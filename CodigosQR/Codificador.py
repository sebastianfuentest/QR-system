import qrcode

def qrCodificador(nombre, apellido, rut):
    img = qrcode.make(nombre+" "+apellido+" "+rut)
    type(img)  # qrcode.image.pil.PilImage
    img.save("./QRCodes/"+rut+".png")

