n = 18

print("Guess the number !!!")
print("Rules :-")
print("(1) Please input only numbers")
print("(2) You have only 9 Guesses")
print("(3) Play the game with logic not with Luck !")

 
i = 1
guesses = []

try_again = True
while(try_again):
    user_input = int(input("Enter the input : "))
    if(user_input == n):
         print("Correct Answer,You Won !!")
         try_again = False
    
    elif(9 in guesses):
         print("Game Over !!!")
         try_again = False

    elif(user_input !=n):
        if(user_input > n):
            print("Its smaller than",user_input)
            i += 1
            guesses.append(i)
        elif(user_input < n):
            print("Its greater than",user_input)
            i+=1
            guesses.append(i)
        try_again = True

print("You took " + str(len(guesses)+1) +" guesses")

 