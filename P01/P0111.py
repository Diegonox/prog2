"""
@author: diego
"""
import random


stack_limit = 20
draw_limit = 3
stacks_to_play_for = [i for i in range(1, stack_limit, draw_limit + 1)]


def draw_matches(stack_of_matches: int):
    print("Current stack of matches", stack_of_matches)
    print("------------------------")
    for i in range(0, stack_of_matches):
        print("===========O")


def user_play(stack_of_matches: int):
    while True:
        try:
            draw_of_user = int(input("How many matches do you want to draw? (1, 2 or 3)"))
            break
        except:
            print("The number is out of range")
    stack_of_matches -= draw_of_user
    return stack_of_matches


'''
Computer tries to play for a number which is in the stack_to_play_for list (1,5,9,13...)
'''
def computer_play(stack_of_matches: int):
    draw_of_computer = 0
    for i in range(1, draw_limit + 1):
        temp_stack_of_matches = stack_of_matches - i
        if temp_stack_of_matches in stacks_to_play_for:
            draw_of_computer = i
            break
        if i == 3:
            draw_of_computer = i
    stack_of_matches -= draw_of_computer
    return stack_of_matches


def check_matches(stack_of_matches: int, player):
    if stack_of_matches <= 0:
        if player == "Computer":
            print("The computer lost")
        else:
            print("You lost")
        return True


def main():
    stack_of_matches = random.randint(10, stack_limit)
    draw_matches(stack_of_matches)
    while True:
        stack_of_matches = user_play(stack_of_matches)
        if check_matches(stack_of_matches, "Player1"):
            break
        draw_matches(stack_of_matches)
        stack_of_matches = computer_play(stack_of_matches)
        if check_matches(stack_of_matches, "Computer"):
            break
        draw_matches(stack_of_matches)
    
    
if __name__ == "__main__":
    main()