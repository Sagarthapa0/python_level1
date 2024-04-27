import random

list=[i for i in range(1,10)]
print("**************** Number Guessing Game***************************")
random_number=random.choice(list)
guessed_number=-1
while guessed_number is not random_number:
   guessed_number=int(input("enter your number : "))
   if guessed_number>random_number :
      print("To high")
   elif guessed_number<random_number :
      print("to low")
   else:
      print("Equal")
print("Guessed Right")      



