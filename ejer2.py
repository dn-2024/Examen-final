from datetime import datetime


def funcionDecoradora(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la funcion a decorar")
        resultado = funcionB(*args, **kwargs)
        print("2. Función ejecutada")
        return resultado
    return funcionC


@funcionDecoradora
def registro(nombre, edad, hora, minuto, n1, n2, n3, n4):
    media = (n1+n2+n3+n4)/4
    print(f"{nombre} de {edad} años registrado a las {hora}horas y {minuto}minutos")
    print("la media es: {}".format(media))


act = datetime.now()
hora_act = act.hour
min_act = act.minute
registro("Pedro", 30, hora_act, min_act, 15, 16, 12, 18)