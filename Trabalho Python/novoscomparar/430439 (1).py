codificado = ""
decodificado = ""
caracter = 0

texto=str(input("Digitar um texto a ser codificado: "))
chave = int(input("Digite a chave numerica para codificar: "))
print("Texto Original.....:{0}".format(texto))

for i in range(0, len(texto)):
  caracter = ord(texto[i])*int(chave/2)
  codificado = codificado+chr(caracter)
print("Texto codificado...: {0}".format(codificado))

for i in range(0, len(codificado)):
  caracter = ord(codificado[i])-chave
  decodificado=decodificado+chr(caracter)
print("Texto decodificado: {0}".format(decodificado))