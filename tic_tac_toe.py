import os
def Board(values):
    # Printing Board By using gameValues 's List
    print(f" {values[0]} | {values[1]} | {values[2]} ")
    print(f"---|---|---")
    print(f" {values[3]} | {values[4]} | {values[5]} ")
    print(f"---|---|---")
    print(f" {values[6]} | {values[7]} | {values[8]} ")

def checkWin(values):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if(values[win[0]] == values[win[1]] == values[win[2]] == 'X'):
            Board(values)
            print("X Won the match")
            return 1

        # if gameValues matches with the pattern and has X then O won the Match
        if(values[win[0]] == values[win[1]] == values[win[2]] == 'O'):
            Board(values)
            print("O Won the match")
            return 0

        # if all places are filled and no one is the winner
        if all(isinstance(item, str) for item in values):
            Board(values)
            return -2
    # return -1 if no one wons
    return -1

if __name__ == '__main__':
    print("Welcome to the Game")
    values=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1

    while(True):
        try:
            if chance == 1:
                Board(values)
                print("\nX's Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with O
                if values[value]!= 'O':
                    values[value] = 'X'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for X")
                    continue
                os.system('CLS')

            if chance == 0:
                Board(values)
                print("\n0's Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with X
                if values[value]!= 'X':
                    values[value] = 'O'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for O")
                    continue
                os.system('CLS')

        except IndexError:
            # exception if Value is not between 0 to 8 
            os.system('CLS')
            print("\nOops!! Please Enter value from 0 - 8\n")
            continue

        # for giving chance to other player
        chance = 1 - chance
        cwin = checkWin(values)
        # Game Draw
        if(cwin == -2):
            print("Game Draw")
            break
        # Match Over
        if(cwin != -1):
            print("Match over")
            break