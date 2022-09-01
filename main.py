import random


def makeBoard():
  ''' This function will create the list for the board.'''

  board = [['-', '-', '-','-','-'], 
           ['-', '-', '-','-','-'],
           ['-', '-', '-','-','-'],
           ['-', '-', '-','-','-'],
           ['-', '-', '-','-','-']]
  return board


def drawBoard(board):
  '''This function will draw the board displayed for the game.'''

  for i in board:
    for j in i:
      print(j,end=" ")
    print()
  

def generateNums(numMines): 
    '''This makes the number values and mines for each spot on the board.'''

    #assigns 0 to every spot in the list mines
    mines = [[0 for row in range(5)] for column in range(5)]
    #creates mines in the list
    for num in range(numMines):
        x = random.randint(0,4)
        y = random.randint(0,4)
        #checks to make sure that there isn't already a mine there
        while mines[x][y] == '*':
            x = random.randint(0,4)
            y = random.randint(0,4)    
        #assigns the mine to the location
        mines[x][y] = '*'
        #this set of code adds one to every square surrounding each mine (the specific square is noted at the end of each line)

        if (y >= 1 and y <= 4) and (x >= 1 and x <= 4):
            if mines[x-1][y-1] != '*':
                mines[x-1][y-1] += 1 # top left

        if (y >= 0 and y <= 4) and (x >= 1 and x <= 4):
            if mines[x-1][y] != '*':
                mines[x-1][y] += 1 # top center

        if (y >= 0 and y <= 3) and (x >= 1 and x <= 4):
            if mines[x-1][y+1] != '*':
              mines[x-1][y+1] += 1 # top right

        if (y >=0 and y <= 3) and (x >= 0 and x <= 4):
            if mines[x][y+1] != '*':
                mines[x][y+1] += 1 # center right
                
        if (y >=0 and y <= 3) and (x >= 0 and x <= 3):
            if mines[x+1][y+1] != '*':
                mines[x+1][y+1] += 1 # bottom right

        if (y >= 0 and y <= 4) and (x >= 0 and x <= 3):
            if mines[x+1][y] != '*':
                mines[x+1][y] += 1 # bottom center
                
        if (y >= 1 and y <= 4) and (x >= 0 and x <= 3):
            if mines[x+1][y-1] != '*':
                mines[x+1][y-1] += 1 # bottom left
                
        if (y >= 1 and y <= 4) and (x >= 0 and x <= 4):
            if mines[x][y-1] != '*':
                mines[x][y-1] += 1 # center left

    return mines


def userTurn(mines, board, numMines):
  '''This function basically runs the game for the user and also determines when it is over.'''

  valid = False
  numDashes = 0
  #This loop will keep the game going until the user either wins or loses.
  while valid == False:  
    #takes in the x-value on the board
    x = input("Which row do you want to check? ")
    #checks to make sure the value is valid
    while x not in "01234":
      print("This input is invalid. Please enter an integer between 0 and 4. ")
      x = input("Which row do you want to check? ")
    x = int(x)
  
    #takes in the y-value on the board
    y = input("Which column do you want to check? ")
    #checks to make sure the value is valid
    while y not in "01234":
      print("This input invalid. Please enter an integer between 0 - 4. ")
      y = input("Which column do you want to check? ")
    y = int(y)
    
    #reassigns the location on the original board to be the value found in the same location in the mines list
    board[x][y] = mines[x][y]
    #draws the updated board
    drawBoard(board)
    #keeps track of the number of non-mines uncovered
    numDashes = numDashes + 1

    #determines if the user has lost by uncovering a mine
    if mines[x][y] == '*':
      print("Game over! ")
      #gives the user the option to keep playing or quit
      ans = input("Want to play again? yes or no: ")
      if ans == 'yes':
        main()
      else:
        valid = True

    #determines if the user has won the game 
    if numMines == 25 - numDashes:
      print("You Win! ")
      #gives the user the option to keep playing or quit
      ans = input("Want to play again? yes or no: ")
      if ans == 'yes':
        main()
      else:
        valid = True


def main():
  '''This function runs the game.'''

  #determines how many mines will be placed in the game
  numMines = input("How many mines do you want? ")
  while numMines not in "1234567890":
    print("That value is invalid! Please try again. ")
    numMines = input("How many mines do you want? ")
  numMines = int(numMines)
  #makes and draws the original board for the user
  board = makeBoard()
  drawBoard(board)
  #creates the numbers and mines for the game
  mines = generateNums(numMines)
  #starts the user's turn
  userTurn(mines, board, numMines)
      
main()
  
