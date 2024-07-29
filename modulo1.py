"""_inputName = input("Qual seu nome?")
if (_inputName != ""):
 _newName =_inputName
print("Seja bem vindo(a) " + _newName) 
print(type(_newName))
_newNameModifiq = bool(_newName)
print(type(_newNameModifiq))"""

"""pergunta = input("Vamos calcular? (sim/não): ")
if pergunta.lower() == "sim":
    numero = float(input("Digite um número: "))
    operacao = input("Qual operação deseja fazer? (+, -, *, /): ")
    outroNumero = float(input("Digite outro número: "))
    
    if operacao == "+":
        print(f"Resultado: {numero + outroNumero}")
    elif operacao == "-":
        print(f"Resultado: {numero - outroNumero}")
    elif operacao == "*":
        print(f"Resultado: {numero * outroNumero}")
    elif operacao == "/":
        print(f"Resultado: {numero / outroNumero}")
    else:
        print("Operação inválida!")
else:
    print("Cálculo cancelado.")
# Basic mathematical operations with Numbers

# Addition
print(5+23)

# Subtraction
print(100-25)

# Multiplication
print(5*10)

# Power/Exponent
# ** operator is equivalent to exponent
print(5**2)

# 5*5 = 5^2 = 5**2 
print(5*5)


# Division (float)
# Return the actual decimal value of division
print(36/4)
print(10/3)         

# Division (int)
# Return an int. If the actual quotient is a decimal value, only whole number is returned 
print(10//3)
print(19//6)

# Modular Division: return the remainder of division
print(10%3)

# Operations with Strings and Characters
print("foo" * 5)
print('x '* 3)
print('x+y * 15') #? 
print('abcd' * 9)"""
_saudacao = "hello world "  
_numero = 5
mensagem = _saudacao + str(_numero)
print(mensagem)

# Fix
print("hello " + str(5))

print("Welcome " "hello " "world.")

# print("cinco" + 5)# ERROR: cannot concatenate an int to a string --> need to cast int to string 
# Comparators: return boolean value

# Equality ==
# Note: MUST be Double equal signs, single equal sign is assignment
print(5 == 5.0)
print(5 == "5")

# Greater than >
print(7 > 1)

# Less than <
print(1.5 < 90)

# Greater than or equal to >=
print(5.0 >= 5)
print(5.0 >= 4)
print(5 >= 13)

# Less than or equal to <=
print(10 <= 10.0)
print(10 <= 20)
print(8 <= 3)

x = 7
y = 49
if (2 * x == y):
    print("y é o double de x")
elif (x**2 == y):
  print("y is the squared of x")
else:
  print("y is NOT double of x")




a = 10
b = 20
# if(a * 2 and a ** 2 > b):
#    print ("10")
if(a + b < 2):
   print("A")
elif(a ** a < b):
   print("100")
elif(a % 2 == 1):
   print(a % 2 == 0)
elif(a * 2 and a ** 2 > b and a ** a > b and a % 2 == 0):
 print("sucesso")
else:
   print("20")
print(a % 2 == 0)
"""O Python NÃO tem uma implementação para os casos de switch,
mas uma maneira de implementar o caso de switch é com o dicionário,
uma estrutura de dados que armazena o par chave-valor (Módulo 3).
As condições de comutação são armazenadas como chaves no dicionário
e as ações armazenadas como o valor.
Se houver uma série de ações para cada caso, considere escrever
uma função para cada caso e usar as chamadas de função como o valor.
A condição padrão é listada manualmente como um valor-chave no get()."""
 
def switcher(number):
 return {
    '0':"Entered 0",
    '1':"Entered 1",
    '2':"Entered 2",
    '3':"Entered 3",
    '4':"Entered 4",
    '5':"Entered 5",
    '6':"Entered 6",
    '7':"Entered 7",
    '8':"Entered 8",
    '9':"Entered 9",
  }.get(number,"Invalid number!")

# input() reads in an user input from stdin
number = input("Dial a number: ")
print(switcher(number))
 