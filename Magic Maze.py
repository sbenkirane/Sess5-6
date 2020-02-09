def main():
    print("You are in the magic maze! Which way to go? (N, S, W, E)")
    print("You have 3 lives, after 5 wrong moves, you lose a life. Be smart... good luck!")

    path = ["S", "S", "N", "W", "E", "S"]
    input_path = []

    moves: int = 0
    correct_moves = 0
    wrong_moves = 0
    life = 3

    for i in range(0, len(path)):

        while True:

            try:

                user_input = input()
                moves += 1

                if user_input in path:
                    input_path.append(user_input)

                if input_path[i] == path[i]:
                    print("You are going the right way!")
                    print(input_path)
                    correct_moves += 1
                    break

                elif input_path[i] != path[i]:
                    wrong_moves += 1
                    input_path.remove(user_input)
                    print("Wrong move, you have to start the maze again!")
                    print(input_path)

                    if wrong_moves == 1:
                        print("You have now made", wrong_moves, "wrong move.")
                    elif wrong_moves > 1:
                        print("You have now made", wrong_moves, "wrong moves.")

                    if wrong_moves == 5:
                        life -= 1
                        print("Lives remaining:", life, "... Be careful!")
                    if wrong_moves == 10:
                        life -= 1
                        print("Life remaining:", life, "... This is your last chance!")
                    if wrong_moves == 15:
                        life -= 1
                        print("You have lost all your lives! Game has restarted. \n")
                        main()

            except ValueError and IndexError:
                print("Invalid direction, please try again!")

    if input_path == path:
        print('\nCongratulations, you have escaped the maze! You made it in', moves, 'moves, and kept', life,
              'lives!')


main()
