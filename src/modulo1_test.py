#Escribir en el módulo de pruebas un test de esta función, visualizando en pantalla el 
# número total de registros leídos, los 3 primeros registros leídos y los 3 últimos registros leídos.

from modulo1 import *

if __name__ == "__main__":
    students = read_placement_data_full_class("data/Data_Full_Class.csv")

    print(students [0:3])
    print(students[-3:])