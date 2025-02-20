import random
import Battleship

position1 = Battleship.ship_position()
row1 = position1[0]
column1 = position1[1]

position2 = Battleship.ship_position()
row2 = position2[0]
column2 = position2[1]

while Battleship.compare(row1, column1, row2, column2) == True:
    position1 = Battleship.ship_position()
    row1 = position1[0]
    column1 = position1[1]

    position2 = Battleship.ship_position()
    row2 = position2[0]
    column2 = position2[1]
    if Battleship.compare(row1, column1, row2, column2) == False:
        break

board = Battleship.battleship_board()
Battleship.broad_mark_ship(board, row2, column2)
Battleship.long_mark_ship(board, row1, column1)
Battleship.print_board(board)

user_coordinates = Battleship.user_input()
row_pick = user_coordinates[0]
column_pick = user_coordinates[1]

hit_result = Battleship.check_hit(row_pick, column_pick, row1, column1, row2, column2)

print(hit_result["message"])
if hit_result["hit_state"]:
    print(f"Hit confirmed at row {hit_result['row'] + 1}, column {hit_result['column'] + 1}.")
else:
    print("No hit recorded.")