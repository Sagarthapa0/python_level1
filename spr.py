import random
spr_dict={
    "1":"Rock",
    "2":"paper",
    "3":"scissor"
}
def print_info():
    print("""
          Choose one of the following:
          1: scissor
          2: paper
          3: rock
          """)

def get_user_choice():
    user_input=None
    while user_input not in list(spr_dict.keys()):
        user_input=input("Enter your choice: ")
    user_choice=spr_dict[user_input]
    return user_choice

def check_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("Draw")
        return
    if computer_choice=="Rock":
        if user_choice=="paper":
            print("You Win!")
        else:
            print("You Lose!")
    elif computer_choice=="paper":
        if user_choice=="Rock":
            print("You Lose")
        else:
            print("You Win")
    else:
        if user_choice=="paper":
            print("You Lose")
        else:
            print("You Win")                    



def ask_to_play_again():
    ans=None
    while ans not in ["yes","no"]:
       ans=input("Do you wanna play again : ")
    if ans == "yes":
        return True
    else:
        return False

play_again=True
while play_again:
    print_info()
    user_choice=get_user_choice()
    computer_choice=spr_dict[random.choice(list(spr_dict.keys()))]
    print("user choice: ", user_choice)
    print("computer choice :", computer_choice)
    check_winner(user_choice,computer_choice)
    play_again=ask_to_play_again()
    