import matplotlib.pyplot as plt
import numpy as np
import general as datos
eje_x = np.arange(0,10)


plt.bar(eje_x,datos.nivel1, width=0.2)
plt.bar(eje_x + 0.2,datos.nivel2, width=0.2, bottom=datos.nivel1)
plt.bar(eje_x + 0.4,datos.nivel3, width=0.2)
plt.bar(eje_x + 0.6,datos.nivel4, width=0.2)
plt.bar(eje_x + 0.8,datos.nivel5, width=0.2)

#plt.show()