import datetime
# now=datetime.datetime.now()
# print(now)

# year=now.year
# print(year)
# year1=now.strftime("%d/%b")
# print(year1)


# tomorrow=datetime.datetime(2024,4,5)
# print(tomorrow)


# Q. guess game with limted time

import random
from datetime import datetime,timedelta

list=[i for i in range(1,10)]
print("**************** Number Guessing Game***************************")
random_number=random.choice(list)
guessed_number=-1
starttime=datetime.now()
while guessed_number is not random_number:
   if starttime < datetime.now() - timedelta(seconds=10):
      print("Time Over")
      break   
   guessed_number=int(input("enter your number : "))
   if guessed_number>random_number :
      print("To high")
   elif guessed_number<random_number :
      print("to low")
   else:
      print("Equal")
print("Guessed Right")      