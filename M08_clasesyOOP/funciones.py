
class Funciones:
    def __init__(self,lista):
        self.lista = lista

    def es_primo(self,n):
        b = True
        for i in range(2,n):
            if (n % i == 0):
                b = False
                break
        return b
    
    def mas_repetido(self,lista):
        dicc = {i:lista.count(i) for i in lista}
        maximo = max(dicc,key=dicc.get)
        cant = max(dicc.values())
        
        return maximo,cant
    
    def convertidor_grados(self,valor,origen,destino):

        if (origen == 'celsius'):
            if (destino == 'celsius'):
                resultado = valor
            elif (destino == 'farenheit'):
                resultado = (valor * 9 / 5) + 32
            else:
                resultado = valor + 273.15

        if (origen == 'farenheit'):
            if (destino == 'celsius'):
                resultado = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                resultado = valor
            else:
                resultado = ((valor - 32) * 5 / 9) + 273.15
        
        if (origen == 'kelvin'):
            if (destino == 'celsius'):
                resultado = valor - 273.15
            elif (destino == 'farenheit'):
                resultado = ((valor - 273.15) * 9 / 5) + 32
            else:
                resultado = valor
        return resultado
    
    def fact(self,n):
        res = 1
        if(type(n) != int or n < 0):
            return ("el valor ingresado es incorrecto")
        elif (n > 0):
            res = n * self.fact(n-1)
        
        return res
    
    def es_primo_list(self):
        for i, elem in enumerate(self.lista):
            if(self.es_primo(elem)):
                print(f'el numero {elem} de la posicion {i} es primo')
            else:
                print(f'el numero {elem} de la posicion {i} no es primo')

    def convertidor_grados_list(self,origen,destino):
        for elem in self.lista :
            print(f'la conversion de {elem} grados {origen} en {destino} es {self.convertidor_grados(elem)}')
    
    def fact_list(self):
        for elem in self.lista:
            print(f'el factorial de {elem} es: {self.fact(elem)}')