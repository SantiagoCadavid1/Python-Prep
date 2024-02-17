#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def es_primo(num):
    """Esta funcion recibe un numero entero y retorna un valor booleano dependiendo si dicho valor es o no primo.

    Args:
        num (entero): Numero a evaluar si es primo o no.

    Returns:
        booleano: Valor booleano, es True si el valor de entrada es primo y False en caso contrario
    """
    for i in range(2,num//2+1):
        if (num%i==0):
            return False
    return True



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def evalListaPrimos(lista):
    """Funcion que evalua que numeros de una lista son enteros

    Args:
        lista (lista): Lista compuesta por numeros enteros

    Returns:
        lista: Lista compuesta por valores booleanos que corresponden a si los valores de la lista de entrada son o no primos
    """    
    result=[]
    for i in lista:
        result.append(es_primo(i))
    return result


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def num_repetido(lista):
    """Esta funcion recibe como argumento una lista y retorno el numero que mas se haya repetido

    Args:
        lista (lista): Lista a evaluar

    Returns:
        entero: Retorna el primer valor que mas veces se haya repetido
    """    
    maximo=0
    numero=lista[0]
    for i in lista:
        actual=0
        for j in lista:
            if j==i:
                actual+=1
        if actual>maximo:
            maximo=actual
            numero=i
    return numero, maximo



# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def conversion(temp, uni_inicial, uni_destino):
    """_summary_

    Args:
        temp (float): Numero real que represente la temperatura en alguna de las unidades
        uni_inicial (string): "Celsius", "Farenheit" o "Kelvin" indicando cual es la unidad a la que se esta dando la temperatura
        uni_destino (string): "Celsius", "Farenheit" o "Kelvin" indicando cual es la temperatura a la que se desea convertir la temperatura inicial

    Returns:
        float: Valor de conversion de la temperatura
    """    
    if (uni_inicial=="Celsius"):
        if(uni_destino=="Celsius"):
            return temp
        elif(uni_destino=="Farenheit"):
            return (temp*9/5)+32
        else:
            return temp+273.15
    elif (uni_inicial=="Farenheit"):
        return conversion((temp-32)*5/9, "Celsius", uni_destino)
    else:
        return conversion(temp-273.15, "Celsius", uni_destino)

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(val):
    if (type(val)==int)and(val>=1):
        if (val>1):
            return val*factorial(val-1)
        else:
            return val
    else:
        return "Para utilizar la funcion factorial ingrese un valor entero positivo"

# In[65]:




