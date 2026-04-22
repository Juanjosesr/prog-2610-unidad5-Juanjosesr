fp = open(".\\archivos\\texto_aleatorio.txt", "r", encoding="utf-8")
texto1 = fp.readlines()
fp.close()

for texto1 in texto1:
    print(texto1[0])