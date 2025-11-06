# Write your solution here

def who_won(game_board: list):
  player1 = 0
  player2 = 0
  for row in game_board:
    for gamePiece in row:
      if gamePiece == 1:
        player1 += 1
      if gamePiece == 2:
        player2 += 1

  if player1 > player2:
    return 1
  elif player1 < player2:
    return 2
  elif player1 == player2:
    return 0

if __name__ == "__main__":
  game_board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
  print(who_won(game_board))
