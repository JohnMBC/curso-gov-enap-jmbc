"""
EXERCISE: implement the switch case example 
using if/else conditions
Prompt: For each digit between 0-9, 
the program will print a confirmation 
for the entered value or print "invalid inputs" 
for all other numbers.
"""
def switcher(key):
  return {
    '0':"zero",
    '1':"value 1",
    '2':"value 2",
    '3':"value 3",
    '4':"value 4",
    '5':"value 5",
    '6':"value 6",
    '7':"value 7",
    '8':"value 8",
    '9':"value 9",
  }.get(key,"Invalid key!")
key = input("Insira um digito (0 a 9): ")
if (key == "0"):
   print(switcher(key))
elif(key =="1"):
   print(switcher(key))
elif(key =="2"):
   print(switcher(key))
elif(key =="3"):
   print(switcher(key))
elif(key =="4"):
   print(switcher(key))
elif(key =="5"):
   print(switcher(key))
elif(key =="6"):
   print(switcher(key))
elif(key =="7"):
   print(switcher(key))
elif(key =="8"):
   print(switcher(key))
elif(key =="9"):
  print(switcher(key))
else:
  print("chave inválida")

