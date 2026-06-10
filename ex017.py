co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(' A hipotenusa vai medir {:.2f}'.format(hi))
###=======------------------------##________________________

import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = math.hypot(co, ca)
print('O valor da hipotenusa vai medir {:.2f}'.format(hi))

##-----------------------------##-------------------------
from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))




