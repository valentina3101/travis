import unittest 
import sut
from unittest.mock import MagicMock
import math

class TestSut(unittest.TestCase):
    def tests_area (self):
        area= sut.area(3,2)
        self.assertTrue(area==6)

    def tests_saludar(self):
        a = 'hola' + 'nombre'
        esperado = 'Hola ' + a
        self.assertTrue(sut.saludar(a) == esperado)

    def test_multiplicar(self):
        self.assertEqual(sut.multiplicar(3,3),9)
        

    def test_sumatoria(self):
        sumatoria = sut.sumatoria([1,2,3,4,5,6,7],6)
        self.assertEqual(sumatoria,21)
        

    def test_productoria(self):
        productoria=sut.productoria([1,2,3,4,5],3)
        self.assertEqual(productoria,6)
        
        
    
    def test_valor_absoluto(self):
        pass


    def test_sumar(self):
        self.assertEqual(sut.sumar(3,6),2)

    def test_costototal(self):
        sut.sumar=MagicMock(return_value= 2)
        a = sut.costototal(1,2)
        self.assertTrue(a)

    
    def test_supercalc(self):
        math.exp=MagicMock(return_value=2)
        math.sqrt=MagicMock(return_value=2)
        a = sut.supercalc(3)
        self.assertTrue(a == 2)
        
    
        
    def tests_comparar_a_menor_que_b(self):
        self.assertEqual(sut.comparar(3,6),"A menor que B")
    
    def test_comparar_a_mayor_que_b(self):
        self.assertNotEqual(sut.comparar(7,1),"B menor que A")

    def test_comparar_a_y_b_son_iguales(self):
        self.assertEqual(sut.comparar(6,6),"A y B son iguales")



if __name__=='__main__':
    unittest.main()
