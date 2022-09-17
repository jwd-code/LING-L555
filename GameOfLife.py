import random






def getLiveNeighborCount(grid, row_ind, col_ind):
    #Top left corner
    if row_ind == 0 and col_ind == 0:
        #print("Top left")
        live_neighbors_count = [grid[row_ind+1][col_ind],    #Checks cell down
                                grid[row_ind+1][col_ind+1],  #Checks down right
                                grid[row_ind][col_ind+1]].count(1) #Checks cell right
    #Bottom left corner
    elif row_ind == (len(grid)-1) and col_ind == 0:
        #print("Bottom left")
        live_neighbors_count = [grid[row_ind-1][col_ind],         #Checks cell up
                                grid[row_ind-1][col_ind+1],        #Checks up right
                                grid[row_ind][col_ind+1]].count(1) #Checks cell right

    #Top right corner
    elif (row_ind == 0) and (col_ind == len(grid[row_ind])-1):
        #print("Top right")
        live_neighbors_count = [grid[row_ind][col_ind-1], #Checks cell left
                                grid[row_ind+1][col_ind-1],  #Checks down left
                                grid[row_ind+1][col_ind]].count(1) #Checks cell down

    #Bottom right corner
    elif row_ind == (len(grid)-1) and (col_ind == len(grid[row_ind])-1):
        #print("Bottom right")
        live_neighbors_count = [grid[row_ind-1][col_ind], #Checks cell up
                               grid[row_ind-1][col_ind-1],  #Checks up left
                               grid[row_ind][col_ind-1]].count(1) #Checks cell left
    


    #Checks all cells in first column that are not in the first row or the last row
    elif row_ind != 0 and row_ind != (len(grid)-1) and col_ind == 0:
        #print("First col, middle row")
        live_neighbors_count = [grid[row_ind-1][col_ind], #Checks cell up
                               grid[row_ind-1][col_ind+1], #Checks up right
                               grid[row_ind][col_ind+1],  #Checks cell right 
                               grid[row_ind+1][col_ind+1],  #Checks down right
                               grid[row_ind+1][col_ind]].count(1) #Checks cell down

    #Check cells only in first row not in first or last column
    
    elif row_ind == 0 and col_ind != 0 and col_ind != (len(grid[row_ind])-1):
        #print("First row, middle cols")
        live_neighbors_count = [grid[row_ind][col_ind-1], #Checks cell left
                                grid[row_ind][col_ind+1],  #Checks cell right
                                grid[row_ind+1][col_ind-1],  #Checks down left
                                grid[row_ind+1][col_ind+1],  #Checks down right
                                grid[row_ind+1][col_ind]].count(1) #Check down

    #Check cells only in last row not in first or last column
    elif row_ind == (len(grid)-1) and col_ind != 0 and col_ind != (len(grid[row_ind])-1):
        #print("Last row, middle cols")
        live_neighbors_count = [grid[row_ind][col_ind-1], #Checks cell left
                                grid[row_ind-1][col_ind-1],  #Checks up left
                                grid[row_ind-1][col_ind], #Checks cell up
                                grid[row_ind-1][col_ind+1], #Checks up right
                                grid[row_ind][col_ind+1]].count(1)  #Checks cell right

    #Checks all cells in last column that are not in first row or last row:
    elif row_ind != 0 and row_ind != (len(grid)-1) and col_ind == (len(grid[row_ind])-1):
        #print("Last col, middle rows")
        live_neighbors_count = [grid[row_ind-1][col_ind], #Checks cell up
                                grid[row_ind-1][col_ind-1],  #Checks up left
                                grid[row_ind][col_ind-1], #Checks cell left
                                grid[row_ind+1][col_ind-1], #Checks cell down left
                                grid[row_ind+1][col_ind]].count(1)


    #  All middle cells
    elif row_ind != 0 and row_ind != (len(grid)-1) and col_ind != 0 and col_ind != (len(grid[row_ind])-1):
        #print("All middle")
        live_neighbors_count = [grid[row_ind][col_ind+1], #Checks cell right
                grid[row_ind][col_ind-1], #Checks cell left
                grid[row_ind-1][col_ind], #Checks cell up
                grid[row_ind+1][col_ind], #Checks cell down
                grid[row_ind+1][col_ind+1],  #Checks down right
                grid[row_ind+1][col_ind-1],  #Checks down left
                grid[row_ind-1][col_ind+1],  #Checks up right
                grid[row_ind-1][col_ind-1]].count(1) #Checks up left
    
    return live_neighbors_count

        
 
def updateGrid(grid, row_ind, col_ind, live_neighbors_count):
    updated_grid = grid 
    old_cell = grid[row_ind][col_ind]

    if old_cell == 1 and live_neighbors_count < 2:
        updated_grid[row_ind][col_ind] = 0
        #print("Died by underpopulation")

    elif old_cell == 1 and live_neighbors_count == 2 or live_neighbors_count == 3:
        updated_grid[row_ind][col_ind] = 1

    elif old_cell == 1 and live_neighbors_count > 3:
        updated_grid[row_ind][col_ind] = 0
        #print("Died by overpopulation")

    elif old_cell == 0 and live_neighbors_count == 3:
        updated_grid[row_ind][col_ind] = 1
        #print("Born at:", row_ind+1, ",", col_ind+1)
        #print("Born by reproduction")

    return updated_grid

def createGrid():
    new_grid = []
    dim_num = int(input("Enter a number 'N' to create an N by N grid:"))
    for i in range(dim_num):
        new_grid.append([])
    for row in new_grid:
        while len(row) < dim_num:
            row.append(random.randint(0,1))
    return new_grid


def playGOL():
    the_grid = createGrid()
    gen_number = int(input("How many generations would you like to run?"))
    print("Starting grid:")
    for row in the_grid:
        print(row)
    print("--------------")

    gen_count = 0
    while gen_count < gen_number:
        for row in the_grid:
            rind = the_grid.index(row)
            cind = -1
            for cell in row:
                cind +=1
                live_count = getLiveNeighborCount(the_grid, row_ind=rind, col_ind=cind)
                #print("Neighbor count:", live_count)
                updated_grid = updateGrid(the_grid, rind, cind, live_count)
            updated_grid = the_grid
        gen_count += 1
            
        
        print("Generation:", gen_count)
        for row in updated_grid:
            print(row)
        print('------------')




playGOL()
    
    


