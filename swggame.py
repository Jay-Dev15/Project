import random
print("wlecome in snake-water-gun game\nbest of luck")
print("For snake enter s \nFor water enter w \nFor gun enter g")
list=["s","w","g"]
n=10
com_point=0
you_point=0
i=0
while i<10:
    _input=input("snake,water,gun")
    _random=random.choice(list)

    if _input==_random:
        print(f"your guess {_input} and computer guess {_random} \n")
        print("It's tie")
#you guess s
    elif _input=="s" and _random=="g":
        com_point=com_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")
    
    elif _input=="s" and _random=="w":
        you_point=you_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("you win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")

#you guess w
    elif _input=="w" and _random=="g":
        you_point=you_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("you win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")
   
    elif _input=="w" and _random=="s":
        com_point=com_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")
     
#you guess g
    elif _input=="g" and _random=="w":
        com_point=com_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("computer win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")
    
    elif _input=="g" and _random=="s":
        you_point=you_point+1
        print(f"your guess {_input} and computer guess {_random} \n")
        print("you win 1 point")
        print(f"computer's points are {com_point} and your points are {you_point}")

    else :
        print("wrong input\nFor snake enter s \nFor water enter w \nFor gun enter g")
    print("________________________________________________________________________________________________")
    i=i+1

print(f"your point is {you_point} and computer point is {com_point}")
if you_point<com_point :
    print("you loss better luck next time")
else:
    print("you win")

print("thank you for playing")