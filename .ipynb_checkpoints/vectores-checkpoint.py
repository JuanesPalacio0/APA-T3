"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Juan Esteban Palacio Ibarra
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
        
""" 1 """
   def __mul__(self, other):
    """
    Sobrecarga del operador asterisco (*) para el producto Hadamard o multiplicación por un escalar.
    """
     if isinstance(other, (int, float, complex)):
        return Vector(uno * other for uno in self)
     else:
        return Vector(uno * otro for uno, otro in zip(self, other))

     else:
        raise TypeError("Operación no soportada entre Vector y " + str(type(other)))


""" 2 """

    def __matmul__(self, other):
        """
        Sobrecarga del operador @ para el producto escalar de dos vectores.
        
        El producto escalar es la suma de los productos de las componentes correspondientes de los vectores.
        """
        
        if isinstance(other, Vector):
            return sum(uno * otro for uno, otro in zip(self.vector, other.vector))
        else:
            raise TypeError("Operación no soportada entre Vector y " + str(type(other)))

""" 3 """

    def __floordiv__(self, other):
        """
        Sobrecarga del operador // para la componente paralela de un vector respecto a otro.
        
        La componente paralela se calcula como (v1·v2) / ||v2||² * v2.
        """
        
        producto_escalar = self @ other
        magnitud_cuadrado = sum(otro ** 2 for otro in other.vector)
        return Vector(producto_escalar / magnitud_cuadrado * uno for uno in other.vector)

""" 4 """ 

     def __mod__(self, other):
        """
        Sobrecarga del operador % para la componente normal de un vector respecto a otro.
        
        La componente normal se calcula como v1 - v1//v2.
        """
        
        componente_paralela = self // other
        return Vector(uno - otro for uno, otro in zip(self.vector, componente_paralela.vector))

""" Pruebas """

import unittest

class TestVectorOperations(unittest.TestCase):

    def test_multiplicacion_escala(self):
        v1 = Vector([1, 2, 3])
        result = v1 * 2
        self.assertEqual(result.vector, [2, 4, 6])

    def test_producto_hadamard(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1 * v2
        self.assertEqual(result.vector, [4, 10, 18])

    def test_producto_escalar(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1 @ v2
        self.assertEqual(result, 32)

    def test_componente_paralela(self):
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])
        result = v1 // v2
        self.assertEqual(result.vector, [1.0, 2.0, 1.0])

    def test_componente_normal(self):
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])
        result = v1 % v2
        self.assertEqual(result.vector, [1.0, -1.0, 1.0])

if __name__ == "__main__":
    unittest.main()





