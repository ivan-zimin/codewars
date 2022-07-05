# RGB To Hex Conversion
# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    hex = ''
    for color in (r, g, b):
        if color < 0:
            hex += ''.join('00')
        elif color in range(0, 256):
            hex += ''.join("{:02x}".format(color).upper())
        else:
            hex += ''.join('FF')
    return(hex)

print(rgb(-20,275,125))

print(rgb(0,0,0))           # 000000
print(rgb(1,2,3))           # 010203
print(rgb(255,255,255))     # FFFFFF
print(rgb(-20,275,125))     # FEFDFC
print(rgb(254,253,252))     # 00FF7D