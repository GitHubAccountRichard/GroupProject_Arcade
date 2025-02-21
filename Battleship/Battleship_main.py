import random
import Battleship

# Generate the first ship's random position
position1 = Battleship.ship_position()
row1 = position1[0]
column1 = position1[1]

# Generate the second ship's random position
position2 = Battleship.ship_position()
row2 = position2[0]
column2 = position2[1]

# Ensure that ships do not overlap
while Battleship.compare(row1, column1, row2, column2) == True:
    # If they overlap, regenerate only the second ship's position
    position2 = Battleship.ship_position()
    row2 = position2[0]
    column2 = position2[1]

# At this point, ship positions are finalized and will no longer change
board = Battleship.battleship_board()
Battleship.broad_mark_ship(board, row2, column2)  # Mark the second ship
Battleship.long_mark_ship(board, row1, column1)  # Mark the first ship
Battleship.print_board(board)

# User guess input
user_coordinates = Battleship.user_input()
row_pick = user_coordinates[0]
column_pick = user_coordinates[1]

# Check if the guess is a hit
hit_result = Battleship.check_hit(row_pick, column_pick, row1, column1, row2, column2)

# Print result
print(hit_result["message"])
if hit_result["hit_state"]:
    print(f"Hit confirmed at row {hit_result['row'] + 1}, column {hit_result['column'] + 1}.")
else:
    print("No hit recorded.")
