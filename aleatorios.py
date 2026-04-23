"""
Generación de números aleatorios mediante LGC (Linear Congruential Generator).
Guillem Perez Sanchez 
QP 2026
"""

class Aleat:

    """
    Clase Aleat: 
    Implementa un generador de números aleatorios en el rango 0≤x≤m usando el método LGC con las características siguientes:
        - Los objetos de la clase serán iteradores, para lo que habrá de definirse el método mágico __next__(), que será el que efectuará la generación en sí  misma y deberá devolver el número aleatorio siguiente.
        - Los valores de m, a y c y la semilla x0 deben ser configurables al crear el objeto (argumentos opcionales del método mágico __init__()). Estos cuatro argumentos opcionales serán indicados, obligatoriamente, por clave (no pueden ser posicionales). Por defecto, los valores de m, a y c serán los usados por el estándar POSIX. El de la semilla será x0=1212121.
        - El método mágico __call__() que sobrecarga la llamada a función, es decir, el uso del objeto como si fuera una función con sus argumentos entre paréntesis, se usará para reiniciar la secuencia con la semilla indicada en su único argumento, que será forzosamente posicional.
    """
    
    def __init__(self, *, m=2**31, a=1103515245, c=12345, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nueva_semilla):
        self.x = nueva_semilla


def aleat(*, m=2**31, a=1103515245, c=12345, x0=1212121):
    
    """
    Implementa el mismo generador de números aleatorios en el rango que en la clase anterior.
    Sigue las condiciones:
        - Los valores de m, a y c y la semilla x0 deben ser configurables al crear la función, y tendrán los mismos valores por defecto que en el caso de la clase Aleat.
        - En caso de enviársele un valor al generador, con su método send(), éste debe reiniciar la secuencia tomando el argumento como semilla de la nueva secuencia.
    """
    
    x = x0
    while True:
        nuevo_x = yield x
        if nuevo_x is not None:
            x = nuevo_x
        x = (a * x + c) % m