# This is the program for rock paper scissor game
# import random module to select random characters from the list
import random
print("Enter the number to select your characters")
print("0 for rock")
print("1 for paper")
print("2 for scissor")
print("only 6 rounds.... let's play the game")
def main():
        k=0
        p=0

        for i in range(1,7):
            # This list for the computer
                list1=["rock","paper","scissor"]
                computer=random.choice(list1)
            # This list for the user
                a=int(input("enter the number:"))
            # This condition is for ....when user input is wrong
                if a>2:
                    print("invalid input")
                    break
                b=list1[a]
                print(f"because of opponent character is {computer} and your character {b}")
                if computer == b:
                    print("both the characters are same play again")
                # This condition is for user in Which user can win this round
                elif (b == "paper" and computer == "rock") or (b == "scissor" and computer == "paper") or (b == "rock" and computer == "scissor"):
                    print("you win the game")
                    k=k+1
                    print(f"you got {k} points")
                else:
                    print("opponent win the game")
                    p=p+1
                    print(f"opponent got {p} points")
        if k>p:
            print(f"your points are {k} you won the game......opponent points are {p}")
        elif p>k:
            print(f"opponent points are {p} opponent won the game......your points are {k}")
        else:
            print(f"your points {k} and opponent points {p} game is draw")

        Repeat=input("want to play again press yes/no\n")
        if Repeat=="yes" or Repeat=="YES" or Repeat=="Yes":
            main()
        else:
            print("bye")
            exit()
main()
                

























