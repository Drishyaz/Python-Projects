print("THE GAME BEGINS!!")

def printBoard(values):
  print("| {} | {} | {} |\n|---|---|---|\n| {} | {} | {} |\n|---|---|---|\n| {} | {} | {} |".format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8]))

def check_winner(player_pos,cur_player):
  soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

  for x in soln:
    if all(y in player_pos[cur_player] for y in x):
      return True
  return False

def check_draw(player_pos):
  if len(player_pos['x']) + len(player_pos['o']) == 9:
      return True
  return False   

def player_name():
  p1 = input("\nPlayer 1(x) enter your name: ")
  p2 = input("Player 2(o) enter your name: ")
  return p1,p2

def printScoreboard(score_board):
  print("--------------------------------")
  print("            SCOREBOARD       ")
  print("--------------------------------")
 
  players = list(score_board.keys())
  print("   ", players[0], "    ", score_board[players[0]])
  print("   ", players[1], "    ", score_board[players[1]])
 
  print("--------------------------------\n")

def play(cur_player):
  values = [' ' for i in range(9)]
  player_pos = {'x':[],'o':[]}
  
  while True:
    printBoard(values)

    #TRY EXCEPTION BLOCK FOR SLOT input
    try:
      print("Player",cur_player,"turn. Which slot?")
      slot = int(input())
    except ValueError:
      print("Wrong input!! Try again!!")
      continue

    #Sanity check for SLOT input
    
    if slot < 1 and slot < 9:
      print("Wrong input!! Try again!!")
      continue

    #Check if the slot hasn't already been occupied
    
    if values[slot-1] != ' ':
      print("Place already filled. Try again!!")
      continue

    #UPDATE GAME INFORMATION
    #Updating grid status
    
    values[slot-1] = cur_player
    player_pos[cur_player].append(slot)

    #FUNCTION CALL FOR CHECKING WHO WINS
    
    if check_winner(player_pos,cur_player):
      printBoard(values)
      print("Player",cur_player,"has won the game!!\n")
      return cur_player

    #FUNCTION CALL FRO CHECKING DRAW GAME
    
    if check_draw(player_pos):
      printBoard(values)
      print("Game drawn\n")
      return 'D'
      
    #SWITCH PLAYER MOVES
    
    if cur_player == 'x':
      cur_player = 'o'
    else:
      cur_player = 'x'

if __name__ == '__main__':
  
  p1,p2 = player_name()
  cur_player = 'x'
  
  score_board = {p1:0,p2:0}
  printScoreboard(score_board)

  while True:
    choice = input("Press Q if you want to Quit or Press C to Continue: ")
    if choice == 'Q':
      print("FINAL SCORES!!")
      printScoreboard(score_board)
      break

    elif choice == 'C':
      pass

    else:
      print("Wrong choice!! Try again!!")
      
    winner = play(cur_player)

    if winner != 'D':
      player_won = winner       #'o'
      if player_won == 'x':
        score_board[p1] = score_board[p1] + 1
      else:
        score_board[p2] = score_board[p2] + 1

  if cur_player == 'x':
      cur_player = 'o'
  else:
      cur_player = 'x'
  
