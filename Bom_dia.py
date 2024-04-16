executar_novamente = True
while executar_novamente == True:
  print("Bom dia Tudo Bem?:")
  resposta = input()
  print("Você quer executar o programa novamente? (S/N)")
  resposta = input()
  if resposta == "S":
   executar_novamente = True
  else:
    executar_novamente = False