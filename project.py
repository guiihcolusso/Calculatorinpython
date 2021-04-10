print("██████████████████████████████████████████")
print("Olá, Bem vindo a Calculadora ")
print()
print("Soma, Subtracao, Vezes, Divisao")
print()
print("Entao Vamos lá :)")
print("██████████████████████████████████████████")

TConta = input("Digite o Tipo da conta : ")

print("\n" * 50)

#Calculo de Mais

if TConta == "Soma" or TConta == "soma" :
    print("██████████SOMA██████████")
    print()
    valor1 = float (input("Digite o Primeiro Valor : "))
    valor2 = float (input("Digite o Segundo Valor : "))


resultado = valor1 + valor2
print("Resultado : ")
print(resultado)



#Calculo de Menos

if  TConta == "Subtracao" or TConta == "subtracao" :
    print("██████████Subtracão██████████")
    print()
    valor1 = float (input("Digite o Primeiro Valor : "))
    valor2 = float (input("Digite o Segundo Valor : "))

resultado = valor1 - valor2
print("Resultado : ")
print(resultado)

#Calculo de Vezes

if TConta == "Vezes" or TConta == "vezes" :
    print("██████████Vezes██████████")
    print()
    valor1 = float (input("Digite o Primeiro Valor : "))
    valor2 = float (input("Digite o Segundo Valor : "))

resultado = valor1 * valor2
print("Resultado : ")
print(resultado)

#Calculo de Divisão

if TConta == "Divisao" or TConta == "divisao" :
    print("██████████Divisão██████████")
    print()
    valor1 = float (input("Digite o Primeiro Valor : "))
    valor2 = float (input("Digite o Segundo Valor : "))

resultado = valor1 / valor2
print("Resultado : ")
print(resultado)

