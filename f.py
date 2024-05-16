def area_retangulo(b,a):
    area =b*a
    return area
def area_triangulo(b=1,a=1):#nomear parametros
    area = b* a/2

#calcular area de retangulo
#base * altura

#calcular area do triangulo retangulo
#base* altura/2
print("Programa para calcular areas")
print("Informe o valor da base ===>")
base = float(input())

print("Informe o valor da altura ==>")
altura = float(input())

menu =''''
Informe o tipo do objeto
(T)riangulo
(R)etangulo
'''
print(menu)
opcao = input().lower()[0]

if opcao == 't':
    resultado,a1,b1 = area_triangulo( a=altura )# obrigado a passar as intruções dentro os parametros
    
elif opcao == 'r':    
    resultado,a1,b1 = area_retangulo( base, altura )
    print("Area é igual a ==> ", resultado)


#trechos de codigos
#pequena e coesa




def area_retangulo( b, a ):    
    area = b * a    
    return area
def area_triangulo( b, a ):    
    area = b * a / 2    
    return area
# Calcular area de retangulo
# # base * altura
# # Calcular area do triangulo 
# retangulo
# # base * altura / 2
print ("PROGRAMA PARA CALCULAR AREAS")
print("Informe o valor da base==>")
base = float(input())
print("Informe o valor da altura==>")
altura = float(input())
menu = """Informe o tipo do objeto(T)riangulo(R)etangulo"""
print(menu)
opcao = input().lower()[0]
if opcao == 't':    
    resultado = area_triangulo( base, altura )
elif opcao == 'r':    
    resultado = area_retangulo( base, altura )
    print("Area é igual a ==> ", resultado)