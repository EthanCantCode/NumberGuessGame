import random

game = True

while game:

    #Random number 1-1000
    rnd = random.randint(1, 100)

    #Holds the random Number
    intRnd = rnd

    print("Guess the number 1-100\n")

    run = True

    #Attempt Counter
    atmp = 0

    while run:

        error = True

        while error:
            try:
                num = int(input())
                error = False
            except:
                print("enter a number")

        #For if number is higher
        if num > intRnd:
            print("\nLower")
            atmp+=1

        #For if number is lower
        elif num < intRnd:
            print("\nHigher")
            atmp+=1

        #Correct Guess
        elif num == intRnd:
            print("\nCorrect Number")
            print("\nThe Number was:")
            print(intRnd)
            print("\nFinal Number of Attemps")
            print(atmp)
            run = False

        #Test lines
        #print("\nThe Number was:")
        #print(intRnd)

    print("Play Again? y/n")

    check = True

    #Checks for a replay
    while check:

        replay = input()

        if replay == "y":
            check = False
            game = True

        elif replay == "n":
            check = False
            game = False
            print("GG")

        else:
            print("Enter valid command! y/n (Case Senstive)")




















