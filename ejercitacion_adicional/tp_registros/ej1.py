"""
Definir los registros para almacenar los siguientes tipos de datos: 
a) Fecha (día, mes, año) 
b) horario (horas, minutos, segundos) 
c) Datos de un producto 
nombre  (cadena de caracteres) 
precio unitario (número real) 
fecha de alta del producto (día, mes, año) 
"""
from dataclasses import dataclass


"""class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __repr__(self):
        return f"dia: {self.dia}, mes: {self.mes}, año: {self.anio}"
"""
@dataclass
class Fecha:
    dia: int
    mes: int
    anio: int

@dataclass
class Horario:
    hora: int
    minutos: int
    segundos: int

@dataclass
class DatosProducto:
    nombre: str
    precio_unitario: int
    fecha_de_alta: Fecha

