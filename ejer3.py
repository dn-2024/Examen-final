from datetime import datetime


def decorador_suma(func):
    def funcC(**kwargs):
        ahora = datetime.now()
        print(f"Se está siendo ejecutado a las {ahora.hour} horas y {ahora.minute} minutos")

        suma = sum(kwargs.values())
        print(f"La suma de los valores es: {suma}")

        resultado = func(**kwargs)
        return resultado
    return funcC


@decorador_suma
def encontrar_mayor(**numeros):
    num_mayor = max(numeros.values())
    print(f"El número mayor es: {num_mayor}")
    return num_mayor
