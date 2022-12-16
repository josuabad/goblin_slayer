import os


def borrar_pantalla():  # El código para borrar la pantalla depende del SO
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")