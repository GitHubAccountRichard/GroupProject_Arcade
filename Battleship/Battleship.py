#First need to define a function which gives us 10 lists with 10 spaces (10x10) matrix

def battleship_board():
    Row_1 = ["[ ]"] * 10
    Row_2 = ["[ ]"] * 10
    Row_3 = ["[ ]"] * 10
    Row_4 = ["[ ]"] * 10
    Row_5 = ["[ ]"] * 10
    Row_6 = ["[ ]"] * 10
    Row_7 = ["[ ]"] * 10
    Row_8 = ["[ ]"] * 10
    Row_9 = ["[ ]"] * 10
    Row_10 = ["[ ]"] * 10
    return [Row_1, Row_2, Row_3, Row_4, Row_5, Row_6, Row_7, Row_8, Row_9, Row_10]





board = battleship_board()
row_number = 1
for row in row_number == 10:
    if row_number == 1:
        print(f"Row10 {' '.join(row)}")
    else:
        print(f"Row {row_number} {' '.join(row)}")
row_number += 1



