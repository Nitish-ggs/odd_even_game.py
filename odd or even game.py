import random

toss = input("Odd or even? choose any one to start the game: ").lower().strip()

comp_toss = random.randint(0,6)

toss_toss = int(input("Enter any digit from 0 to 6 to choose the winner! : "))

if (toss == "even" and ((comp_toss+toss_toss)%2 == 0)) or (toss == "odd" and ((comp_toss+toss_toss)%2 != 0)):
    print("You won the toss")

    user_winchoice = input("Do u want to bat or bowl?").lower().strip()

    if user_winchoice == "bat":
        score_user = 0
        wicket_comp = 3

        while wicket_comp != 0:
            bowler = random.randint(0,6)
            batsman = int(input("what do u want to bat?(input a number btw 0-6):"))

            if batsman == bowler:
                print("You lost a wicket")
                wicket_comp -= 1

            else:
                score_user += batsman
                print(f"Total score is {score_user} and wickets remaining is {wicket_comp}")

        print(f"Final score of first innings is {score_user} and onto the next innings where target is", score_user +1)
        wicket_user = 3
        score_comp = 0
        while wicket_user != 0:

            bowler = int(input("what do u want to bowl?(input a number btw 0-6): "))
            batsman = random.randint(0,6)

            if batsman == bowler:
                print("You got a wicket")
                wicket_user -= 1

            else:
                score_comp += batsman
                print(f"Total score is {score_comp} and wickets remaining is {wicket_user}")

        if wicket_user == 0 and wicket_comp == 0:

            if score_comp > score_user:
                print("You lost against computer")

            else:
                print("You won against the computer")


    else: # user choice is bowling

        score_comp = 0
        wicket_user = 3
        
        while wicket_user != 0:

            bowler = int(input("what do u want to bowl?(input a number btw 0-6): "))
            batsman = random.randint(0,6)

            if batsman == bowler:
                print("You got a wicket")
                wicket_user -= 1

            else:
                score_comp += batsman
                print(f"Total score is {score_comp} and wickets remaining is {wicket_user}") 
        
        print(f"Final score of first innings is {score_comp} and onto the next innings where target is", score_comp +1)

         # user is batting 

        if wicket_user == 0:

            wicket_comp = 3
            score_user = 0
            while wicket_comp != 0:

                bowler = random.randint(0,6)
                batsman = int(input("what do u want to bat?(input a number btw 0-6):"))
                
                if batsman == bowler:
                    print("You lost a wicket")
                    wicket_comp -= 1

                else:
                    score_user += batsman
                    print(f"Total score is {score_user} and wickets remaining is {wicket_comp}")
            
            if wicket_user == 0 and wicket_comp == 0:

                if score_comp > score_user:
                    print("You lost against computer")

                else:
                    print("You won against the computer")
        

else:
    print("Computer won the toss")
    computer_choice = random.choice(["bat","bowl"])
    print(f"computer chose to {computer_choice}")
    if computer_choice == "bat":

        score_comp = 0
        wickets_user = 3
        
        while wickets_user != 0:

            batsman = random.randint(0,6)
            bowler = int(input("what do u want to bowl?(input a number btw 0-6): "))

            if batsman == bowler:
                
                print("You got a wicket!!")
                wickets_user -= 1

            else:
                score_comp += batsman
                print(f"Total score is {score_comp} and wickets remaining is {wickets_user}")

        print(f"Final score of first innings is {score_comp} and onto the next innings where target is", score_comp +1)

        if wickets_user == 0:
            
            #comp is bowling
            score_user = 0
            wicket_comp = 3
            while wicket_comp != 0:

                batsman = int(input("what do u want to bat?(input a number btw 0-6): "))
                bowler = random.randint(0,6)

                if batsman == bowler:
                
                    print("You lost a wicket!!")
                    wicket_comp -= 1

                else:
                    score_user += batsman
                    print(f"Total score is {score_user} and wickets remaining is {wicket_comp}")
                
            if wickets_user == 0 and wicket_comp == 0:

                if score_comp > score_user:
                    print("You lost against computer")

                else:
                    print("You won against the computer")
           
    else:
        score_user = 0
        wicket_comp = 3

        while wicket_comp != 0:
            bowler = random.randint(0,6)
            batsman = int(input("what do u want to bat?(input a number btw 0-6):"))

            if batsman == bowler:
                print("You lost a wicket")
                wicket_comp -= 1

            else:
                score_user += batsman
                print(f"Total score is {score_user} and wickets remaining is {wicket_comp}")

        print(f"Final score of first innings is {score_user} and onto the next innings where target is", score_user +1)
        wicket_user = 3
        score_comp = 0
        while wicket_user != 0:

            bowler = int(input("what do u want to bowl?(input a number btw 0-6): "))
            batsman = random.randint(0,6)

            if batsman == bowler:
                print("You got a wicket")
                wicket_user -= 1

            else:
                score_comp += batsman
                print(f"Total score is {score_comp} and wickets remaining is {wicket_user}")

        if wicket_user == 0 and wicket_comp == 0:

            if score_comp > score_user:
                print("You lost against computer")

            else:
                print("You won against the computer")

