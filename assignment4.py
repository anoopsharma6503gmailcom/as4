#ques1

marks = int(input('enter your marks: '))
if marks < 25 and marks >=0:
    print("you have scored  F grade.")
elif marks >= 25 and marks <45:
    print("you have scored  E grade.")
elif marks >= 45 and marks <50:
    print("you have scored  D grade.")
elif marks >= 50 and marks <60:
    print("you have scored  C grade.")
elif marks >= 60 and marks <80:
    print("you have scored  B grade.")
elif marks >= 80 and marks <= 100:
    print("you have scored  A grade.")
else:
    print("please enter a valid marks !")
    
 #ques2
    
  year = int(input("enter the year: "))
if year % 4 == 0 and year % 100 !=0:
    print("The year is a leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print("the year is a leap year")
else: 
    print("not a leap year")

#Question 3
#Multiplication game

import random
for i in range(1,11,1):
    m=random.randrange(1,10,1) #Generates a random value from 1 to 10
    n=random.randrange(1,10,1) #Generates a random value from 1 to 10
    ans=int(input((f"Question {i}: {m}*{n} = ")))
    if m*n==ans:
    # if the answer is correct print right and start the next iteration
        print("Right!")
        continue
    else:
    # if the answer is incorrect print wrong and start the next iteration
        print("Wrong. The answer is ",m*n)
        continue

#Question 4
#Halloween Candy
n=1
while n<200:
    if n%5==2 and n%6==3 and n%7==2:
        print("Number of candies in the box are",n)
        break
    else:
        n+=1
