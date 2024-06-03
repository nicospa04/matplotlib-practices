import matplotlib.pyplot as plt
import general as datos
import numpy as np
ejeX = np.arange(0,10)

plt.barh(ejeX,datos.nivel1, height=0.2)
plt.barh(ejeX + 0.2,datos.nivel2, height=0.2)
plt.barh(ejeX + 0.4,datos.nivel3, height=0.2)
plt.barh(ejeX + 0.6,datos.nivel4, height=0.2)
plt.barh(ejeX + 0.8,datos.nivel5, height=0.2)

#plt.show()

