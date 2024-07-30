print("Archivo dos __name__ es ejecutado: {}" .format(__name__))

def function_three():
   print("Function three es ejecutada")

if __name__ == "__main__":
   print("Archivo dos ejecutado cuando se ejecuta directamente")
else:
   print("Archivo uno es ejecutado cuando es importado")