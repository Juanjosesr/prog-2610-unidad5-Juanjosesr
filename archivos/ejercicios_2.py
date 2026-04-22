fp = open(".\\archivos\\texto_aleatorio.txt", "r", encoding="utf-8")
texto1 = fp.readlines()
print(texto1[0:5][1])