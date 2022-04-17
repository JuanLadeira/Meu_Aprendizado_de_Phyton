from math import cos,sin,tan,ceil,radians
a = float(input('Digite o valor do angulo'))
sen = sin(radians(a))
co = cos(radians(a))
ta = tan(radians(a))

print('O valor do sen do angulo informado é {:.2f},o valor do cosseno é {:.2f} e a tangente é {:.2f} '.format(sen,co,ta))

