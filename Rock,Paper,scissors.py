#Import the library, random
import random

print("""
                          ====================
                             Rock Paper Scissors
                          ====================  
""")
while True:
#Use random library to let computer choose one number b/w 1 and 3
    computer = random.randint(1,3)
    computer_chose=""
    if computer == 1:
        computer_chose="✊"
    elif computer == 2:
        computer_chose="✋"
    elif computer == 3:
        computer_chose="✌"
    else:
        computer_chose="Nothing"

    player = input("""\n================
1) ✊
2) ✋
3) ✌
Pick a number (write q or quit to quit) : """)
   
    if player.isdigit():
        player = int(player)

        if player in[1,2,3]:
            if player == 1:
                print("You chose: ✊")
                print(f"Computer chose: {computer_chose}")
                if player == 1 and computer == 1:
                    print("It's a tie!")
                elif player ==1 and computer ==2:
                    print("Computer won!")
                elif player ==1 and computer ==3:
                    print("You won!")
                elif player ==2 and computer==1:
                    print("You won!")
                elif player ==2 and computer==2:
                    print("It's a tie!")
                elif player ==2 and computer==3:
                    print("Computer won!")
                elif player==3 and computer==1:
                    print("Computer won!")
                elif player==3 and computer==2:
                    print("You won!")
                elif player==3 and computer==3:
                    print("It's a tie!")
                else:
                    print("It's a tie!")
                    
            elif player == 2:
                print("You chose: ✋")
                print(f"Computer chose: {computer_chose}")
                if player == 1 and computer == 1:
                    print("It's a tie!")
                elif player ==1 and computer ==2:
                    print("Computer won!")
                elif player ==1 and computer ==3:
                    print("You won!")
                elif player ==2 and computer==1:
                    print("You won!")
                elif player ==2 and computer==2:
                    print("It's a tie!")
                elif player ==2 and computer==3:
                    print("Computer won!")
                elif player==3 and computer==1:
                    print("Computer won!")
                elif player==3 and computer==2:
                    print("You won!")
                elif player==3 and computer==3:
                    print("It's a tie!")
                else:
                    print("It's a tie!")
            elif player == 3:
                print("You chose: ✌")
                print(f"Computer chose: {computer_chose}")
                if player == 1 and computer == 1:
                    print("It's a tie!")
                elif player ==1 and computer ==2:
                    print("Computer won!")
                elif player ==1 and computer ==3:
                    print("You won!")
                elif player ==2 and computer==1:
                    print("You won!")
                elif player ==2 and computer==2:
                    print("It's a tie!")
                elif player ==2 and computer==3:
                    print("Computer won!")
                elif player==3 and computer==1:
                    print("Computer won!")
                elif player==3 and computer==2:
                    print("You won!")
                elif player==3 and computer==3:
                    print("It's a tie!")
                else:
                    print("It's a tie!")
                    
        else:
            print("Invalid Input! \nPlease write a number 'b/w 1 and 3'")
    elif player == "q" or player == "quit" or player == "exit" or player == "e":
        print("Ok! exiting...")
        break
    else:
        print("Invalid Input! \nPlease write a 'number' b/w 1 and 3")
        
            
            
