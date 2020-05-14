from random_word import RandomWords
r = RandomWords()
while True:
    pick = r.get_random_word(hasDictionaryDef = "true")
    answer = pick.lower()
    print("The word I am thinking of has " + str(len(answer)) + " letters.")
    print("Guess a letter!")
    #print(answer)
    guess1 = input()
    chance = 6

    #this is needed in case guess is found in multiple places
    index = -1


    #blanks the same length as answer
    empty = ["_"] * len(answer)


    while chance > 0:
        occur = list(answer).count(guess1)
        #print(occur)

        if str(guess1) in empty:
            print("You have already guessed " + guess1)

        elif guess1 == " " or False:
            print("You have not entered a letter!")

            
        elif occur:
            for i in range(occur):
                index = (list(answer)).index(guess1,index+1)
                empty[index] = guess1
                print("".join(empty))
            index = -1

        else:
            chance -= 1
            print("Nope! You have " + str(chance) + " chances left.")
       
        if chance == 0:
            print("Sorry, You lose!  The word was " + answer)
            break
        
        elif "_" not in empty:
            print("You Win")
            break

        guess1 = input()

 
    print("Want to play again?")
    answer = input()
    if answer == "yes":
        True
    elif answer == "no":
        print("ok, goodbye!")
        break
    else:
        print("yes or no?")


    
    
