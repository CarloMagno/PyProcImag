'''
Created on 13/10/2012

@author: M Barrientos Fdez <miguelonbf@gmail.com>; JC Ruiz Rico <bocabyte17@hotmail.com>
'''
import Image

def pixelToNeg(rgbTupla):
    '''
    Convierte un pixel RGB a negativo.
    @return: 3-Tuple
    '''
    R = rgbTupla[0]
    G = rgbTupla[1]
    B = rgbTupla[2]
    
    outRed   = 255-R
    outGreen = 255-G
    outBlue  = 255-B
    
    return (outRed, outGreen, outBlue)    

def pixelToSepia(rgbTupla):
    '''
    Convierte un pixel RGB a tonos de sepia.
    @return: Tupla de 3 elementos ([0..255], [0..255], [0..255])
    '''
    R = rgbTupla[0]
    G = rgbTupla[1]
    B = rgbTupla[2]
    
    outRed   = min(R*0.393 + G*0.769 + B*0.189, 255)*1.15
    outGreen = min(R*0.349 + G*0.686 + B*0.168, 255)
    outBlue  = min(R*0.272 + G*0.534 + B*0.131, 255)
    
    return (int(outRed), int(outGreen), int(outBlue))    

def pixelToGrisMedia(rgbTupla):
    '''
    Convierte un pixel RGB a tono de gris.
    @return: [0..255]
    '''
    R = rgbTupla[0]
    G = rgbTupla[1]
    B = rgbTupla[2]
    
    # Media aritmetica.
    coefR = 0.333
    coefG = 0.333
    coefB = 0.333
    res = coefR*R + coefG*G + coefB*B
    
    return res
    
def pixelToGrisLight(rgbTupla):
    '''
    Convierte un pixel RGB a tono de gris.
    @return: [0..255]
    '''
    R = rgbTupla[0]
    G = rgbTupla[1]
    B = rgbTupla[2]

    # Lightness
    res = (max([R,G,B])+min([R,G,B]))/2
    
    return res    

def pixelToGrisLum(rgbTupla):
    '''
    Convierte un pixel RGB a tono de gris.
    @return: [0..255]
    '''
    R = rgbTupla[0]
    G = rgbTupla[1]
    B = rgbTupla[2]
    
    coefR = 0.21
    coefG = 0.71
    coefB = 0.08
    
    # Luminosity
    res = coefR*R + coefG*G + coefB*B
    
    return res    

##########################
#######  MAIN  ###########
##########################
if __name__ == '__main__':
   #nombreImagen = "the-simpsons.png"    
    nombreImagen = "lowcontrast4.jpg"
    original = Image.open(nombreImagen)
    modoL   = "L"     # Si convertimos a tonos de gris.
    modoRGB = "RGB" # Si convertimos a tonos de sepia o negativo.
    
    # Creacion de imagenes.
    nuevaGrisMedia = Image.new(modoL, original.size)
    nuevaGrisLight = Image.new(modoL, original.size)
    nuevaGrisLum   = Image.new(modoL, original.size)
    
    nuevaSepia = Image.new(modoRGB, original.size)
    nuevaNegat = Image.new(modoRGB, original.size)
    
    n = original.size[0]
    m = original.size[1]
    
    for x in range(n):
        for y in range(m):
            origPixel = original.getpixel((x,y))
            # Negativo y sepia.
            nuevaNegat.putpixel((x,y), pixelToNeg(origPixel))
            nuevaSepia.putpixel((x,y), pixelToSepia(origPixel))
            # Grises.
            nuevaGrisMedia.putpixel((x,y), pixelToGrisMedia(origPixel))
            nuevaGrisLight.putpixel((x,y), pixelToGrisLight(origPixel))
            nuevaGrisLum.putpixel((x,y), pixelToGrisLum(origPixel))
            
    # Guarda imagenes.
    nuevaSepia.save("the-simpsons-sepia.png")
    nuevaGrisMedia.save("the-simpsons-greyMedia.png")
    nuevaGrisLight.save("the-simpsons-greyLight.png")
    nuevaGrisLum.save("the-simpsons-greyLum.png")
    nuevaNegat.save("the-simpsons-neg.png")

    # Muestra las imagenes guardadas.
    original.show()
    nuevaGrisMedia.show()
    nuevaGrisLight.show()
    nuevaGrisLum.show()
    nuevaSepia.show() 
    nuevaNegat.show()
    