#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:




# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:





# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:





# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:






# In[13]:






# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:

import sys


sys.path.append('..\\M07_funciones')
import Prep_Course_Homework_07 as funciones
#print(sys.path)

class Operaciones():
    def __init__(self,lista):
        self.lista=[]
        for i in lista:
            if (type(i)!=int):
                raise ValueError("El valor del elemento {} no corresponde a un entero".format(i))
            else:
                self.lista.append(i)
        
    def es_primo(self):
        
        for i, j in zip(self.lista,funciones.evalListaPrimos(self.lista)):
            if j:
                print("El numero {} es primo".format(i))
            else:
                print("El numero {} no es primo".format(i))
    
    def moda(self):
        numero, maximo = funciones.num_repetido(self.lista)
        print("El numero que mas se repite de la listas es {} repitiendose {} veces".format(numero, maximo))
        
    def conversion(self,index=0,origen="Celsius",destino="Farenheit"):
        print("Si la temperatura en {} es {} entonces en {} es {}".format(origen,self.lista[index],destino,funciones.conversion(self.lista[index],origen,destino)))
        
    def factorial(self,index=0):
        print("El factorial de {} es igual a {}".format(self.lista[index],funciones.factorial(self.lista[index])))



# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:





# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:




# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:




