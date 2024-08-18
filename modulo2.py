"""
The variable i serves as the counter over the RANGE of [0,10), 
inclusive of lower but exclusive of upper bound.

The lower bound of 0 does NOT need to be specify;
it is implemented by default unless another lower bound is specified.

Also by default, if there does NOT exists a third parameter for range(), 
then i increments by 1. 
"""
for i in range(10):
    print(i)

"""
This examples specifies a lower bound that differs from the default value of 0.

The order of the parameter is ALWAYS:
 1. Starting position, inclusive
 2. Stopping position, exclusive
 3. Incremental value


In this example, x starts at the value of 2 and stops at 9 inclusively, or 10 exclusive, 
with x increments by 1 with each iteration.
"""
 
for x in range(2, 10):
   print(x)

"""
The third parameter in range() defines the number of steps to increment the counter.

In this example, x starts at the value of 0 and stops at 9 inclusively, or 10 exclusive, 
with x increments by 3 with each iteration.
"""

for i in range(0, 10, 3):
    print(i)

"""
forEeach loop over the each character in a string.

In this example, the variable 'i' represents every element/character of 'hello.'
In this example, the variable 'i' represents every element/character of 'Johnny.'
In this example, the variable 'i' represents every element/character of 'Programador.'
"""
for i in ("hello","Johnny","programador"):
 print(i)

for i in (" hello Johnny programador"):
 print(i)

saudacao = ("hello Johnny programador")
print(saudacao.split())

"""
We could also iterate over the string by index.
Consider the following example that iterates over the string by index, so printing every element in the string. 
"""
nome = "Johnny Michael Borges Carvalho"
for i in range(0, len(nome),  1 ):
    print(str(i) + " indice da letra: " + nome[i])

"""
We could also iterate over the string by index.

Consider the following example that iterates over the string by index,
starting at index 0 and ending at the last element, with the counter increments by 2, 
so ONLY printing every other element in the string. 
"""
frase = "J-e-s-u-s-C-r-i-s-t-o-r-e-i-n-a"
for i in range(0, len(frase), 2):
   print(str(i)+ " É o indice da letra: "+ frase[i])

# Note: without updating the variable in the while loop,
# this will be an INFINITE loop!!
count = 0
while(count < 10):
  print(count)
# IMPORTANT!!! Updating the counter!
  count += 1

"""Considere um programa que ecoe o input do usuário, exceto pelo "end"
   O programa roda infinitamente, exceto quando o usuário insere "end" para terminá-lo.
"""
 
while True:
      user = input("Enter somenthing to be repeated: ")
      if user == "end":
         print("Terminate the program!!!") 
         break
      print(user)

       
      
       
      
    



























 
            