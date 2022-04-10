import time
import copy
import arrays



def solve_sure(array, xd, yd):
    for x in range(xd, 9):
        for y in range(yd, 9):
            if array[x][y] == 0:
                list_of_possible = []
                for z in range(1, 10):
                    if possible(array=array, x=x, y=y, n=z):
                        list_of_possible.append(z)
                    if len(list_of_possible) >= 2:
                        break
                if len(list_of_possible) == 1:
                    array[x][y] = list_of_possible[0]
    return array


# Part 1 of algorithm
def possible(array, x, y, n):  # in array[x][y] is possible number: [n]? Return bool
    for array_row in range(9):
        if array[x][array_row] == n:
            return False
    for array_column in range(9):
        if array[array_column][y] == n:
            return False
    x1 = ((x // 3) * 3)
    y1 = ((y // 3) * 3)
    for square_row in range(3):
        for square_column in range(3):
            if array[x1 + square_row][y1 + square_column] == n:
                return False
    return True


# Print 9x9 matrix with division line
def draw(array):
    for array_row in range(9):
        row = ''
        for array_column in range(9):
            if array_column == 2 or array_column == 5:
                row += f'{array[array_row][array_column]}| '
            else:
                row += f'{array[array_row][array_column]} '
        print(row)
        if array_row == 2 or array_row == 5:
            print('-------------------')


# Get smallest matrix coordinates with value and possible values. 0 ===> {matrix[x][y] == 0}
def find_numbers(sudoku):
    list_od_possibles = []
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                list_of_possible = []
                for z in range(1, 10):
                    if possible(array=sudoku, x=x, y=y, n=z):
                        list_of_possible.append(z)
                list_od_possibles.append([list_of_possible, [x, y]])
                return list_od_possibles
    return list_od_possibles


# Recursion algorithm, call itself to paste possible number to matrix.
def solve(array1):
    global array_of_arrays
    global iterations

    array_of_arrays.append(array1)
    iterations += 1

    array = []
    for i in range(9):
        array.append(list(array1[i]))

    List_Of_Numbers_ToPaste = find_numbers(array)

    if len(List_Of_Numbers_ToPaste) != 0 or List_Of_Numbers_ToPaste != []:

        pos_xy = List_Of_Numbers_ToPaste[0][0]
        x = List_Of_Numbers_ToPaste[0][1][0]
        y = List_Of_Numbers_ToPaste[0][1][1]

        for i in pos_xy:
            for id in range(9):
                array[id] = list(array1[id])

            array[x][y] = i
            array = solve_sure(array, x - 1, y - 1)
            array = solve(array)

            zero_exist = False
            for ii in range(x, 9):
                for jj in range(y, 9):
                    if array[ii][jj] == 0:
                        zero_exist = True
                        break
                if zero_exist:
                    break
            if not zero_exist:
                break
    return array


if __name__ == '__main__':
    array_of_arrays = []
    iterations = 0
    try:
        number = int(input("What sudoku you want to solve? (give number from arrays.py)"))
    except:
        print("This is not a number")
        exit()

    print('Busy...')

    start = time.perf_counter()
    ab = copy.deepcopy(solve(arrays.arrays[number]))
    end = time.perf_counter()
    print(f'Time: {end - start}, iterations:{iterations}')

    draw(ab)






