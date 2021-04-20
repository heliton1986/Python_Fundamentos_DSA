# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
def soma(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\nSelecione o número da operação: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("\nDigite sua operação: (1/2/3/4): ")

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))

if operacao == "1":
    print("\n")
    print(f"{num1} + {num2} = {soma(num1, num2)}")
    print("\n")
    
elif operacao == "2":
    print("\n")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print("\n")
    
elif operacao == "3":
    print("\n")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print("\n")
    
elif operacao == "4":
    print("\n")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    print("\n")
    
else:
    print("\nOperação Inválida!")