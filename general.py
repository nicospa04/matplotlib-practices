import matplotlib.pyplot as plt
import numpy as np

años = ["2015", "2016", "2017", "2018", "2019",
        "2020", "2021", "2022", "2023", "2024"]

nivel1 =  np.random.rand(10) * 100
nivel2 =  np.random.rand(10) * 200 + 100
nivel3 =  np.random.rand(10) * 300 + 200
nivel4 =  np.random.rand(10) * 400 + 300
nivel5 =  np.random.rand(10) * 500 + 400

#plt.plot(eje x, eje y)
#plt.plot(años, nivel1, label = "Nivel 1", color="red", marker="<", linestyle = "-")
#plt.plot(años, nivel2, label = "Nivel 2", color="green", marker="*", linestyle = "--")
#plt.plot(años, nivel3, label = "Nivel 3", color="purple", marker="x", linestyle = ":")
#plt.plot(años, nivel4, label = "Nivel 4", color = "black", marker="o", linestyle = "-.")
#plt.plot(años,nivel5, label = "Nivel 5", color = "blue", marker = "s", linestyle = " ")

#Activar leyendas (labels)
plt.legend()

#Titulo del gráfico	
plt.title("Niveles de algo por año")

#Etiquetas de los ejes
plt.xlabel("Años")
plt.ylabel("Niveles")

#Personalizar Eje de puntaje de 0 a 1000 en incrementos de 50
plt.yticks(np.arange(0, 750, 50))

#Activar cuadricula
plt.grid()

#Activar ticks menores
plt.minorticks_on()


#plt.show()




