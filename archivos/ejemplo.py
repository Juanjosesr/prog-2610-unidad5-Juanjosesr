# Abre (o crea) un archivo en modo escritura
mi_archivo = open(".\\archivos\\saludo.txt", "w")
mi_archivo.write("Hola, mundo!")
mi_archivo.close() # ¡Muy importante cerrar!