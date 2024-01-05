
class Funciones:
    def __init__(self,lista):
        if(type(lista) != list):
            self.lista = []
            raise ValueError('solo se permiten listas de numeros enteros')
        
        else:
            self.lista = lista

    def es_primo(self,n):
        b = True
        for i in range(2,n):
            if (n % i == 0):
                b = False
                break
        return b
    
    def mas_repetido(self):
        dicc = {i:self.lista.count(i) for i in self.lista}
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
        res = []
        for i, elem in enumerate(self.lista):
            if(self.es_primo(elem)):
                res.append(True)
            else:
                res.append(False)
        return res

    def convertidor_grados_list(self,origen,destino):
        valores_esperados =  ['celsius','kelvin','farenheit']
        res = []
        if(origen not in valores_esperados and destino not in valores_esperados):
            print(f'los valores esperados son: {valores_esperados}')
            return None
        for elem in self.lista :
            res.append(self.convertidor_grados(elem,origen,destino))
        return res
    
    def fact_list(self):
        res = []
        for elem in self.lista:
            res.append(self.fact(elem))
        return res