from log import log_decorator
from timer import time_measure_decorator
from hello import hello

# Decorador para logar a execução da função
@hello
def soma(x, y):
    return x + y

soma(2,3)
soma(2, "3")