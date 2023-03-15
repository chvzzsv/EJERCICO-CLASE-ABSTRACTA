from abc import ABC, abstractmethod

class ClaseAbstracta(ABC):
    @abstractmethod
    def datos(self):
        pass
    
        
class Persona(ClaseAbstracta):
    def __init__(self, nombre, edad, genero):
        self.nombre= nombre
        self.edad= edad
        self.genero= genero

    def datos(self):
        return 'El nombre de la persona es {} tiene la edad de {} años, género {}'.format(self.nombre, self.edad, self.genero)
    
class Animal(ClaseAbstracta):
    def __init__(self, nombre, meses):
        self.nombre= nombre
        self.meses= meses

    def datos(self):
        return 'El nombre del animal es {}, tiene {} meses'.format(self.nombre, self.meses)

class Tienda(ClaseAbstracta):
    def __init__(self, productoPrecio):
        self.productoPrecio= productoPrecio

    def datos(self):
        return 'La leche cuesta ${} en el super selectos'.format(self.productoPrecio)
    
Javier = Persona('Enrique', 20, 'Masculino')
Perro = Animal('Kaiser', 3)
Super = Tienda(5)
print(Javier.datos())
print(Perro.datos())
print(Super.datos())