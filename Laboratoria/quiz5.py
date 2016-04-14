#crean un programa que pida en una función nombre y edad  y
#  otra función  de las guarde en un CSV
import doctest
import unittest
import csv

def agregar ():
    nom = input("Ingrese Nombre: ")
    edad = int(input("Ingrese su Edad: "))
    guardar(nom, edad)

def guardar (nom, edad):
    datos = open("Infor.csv", "a+", newline='')
    escr = csv.writer(datos)
    escr.writerow([nom, edad])
    datos.close()
    return True

agregar()

class SimplisticTest(unittest.TestCase):

    def test(self):
       self.assertTrue(guardar("nome", 2))

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    doctest.testmod()