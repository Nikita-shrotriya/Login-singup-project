import random
digit=5
name=input("enter your name")
print("*******************",name,"***************")
print("WELL COME TO COWS AND BULLS GAME")
def getSecretNum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getSecretNum()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return secret_num
def check_guess():
    bull=[]
    cow=[]
    num=getclues()
    i=0
    print(num)
    maxguess=10
    while maxguess>0:
        guess=int(input("enter your guess="))
        position=int(input("enter the position of your number="))
        print("-----------------------")
        if  guess in num:
            index = num.index(guess)
            if index== position: 
                if guess not in bull:
                    bull.insert(index,guess)
                    print("Bull ",bull)
                else:
                    print("You Already Used This digit Try  any Different digit")
            else:
                cow.append(guess)
                print("Cow, This number is in list you can reuse it",cow)
        if bull==num:
            print(name,"Congractulations you win the game ")
            break 
        maxguess-=1
        print(maxguess,"Turns are left")
    else:
        print("You ran out your tries, You Loose The Game")   
    return bull
check_guess()
def play_again():
    while True:
        again=input("If you Want to play again press y for yes or N of No=") 
        if again=="y":
            check_guess()
        else:
            break 
play_again()