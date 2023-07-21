#Tentei usar TAB para identação, mas retornava erro por algum motivo

import time

#Função que cria o primeiro tabuleiro
def first_gen():
 board = [[0 for i in range(cols)] for i in range(rows)]
 print_board(board)
 stop = input("Deseja inserir células? [Y/N]    ")
 while stop != "N":
  row = int(input("Insira a linha da célula viva   ")) - 1
  col = int(input("Insira a coluna da célula viva   ")) - 1
  if 0 <= row <= rows and 0 <= col <= cols:
   board[row][col] = 1
  print_board(board)
  stop = input("Deseja continuar inserindo? [Y/N]   ")
 return board

#Função para calcular próxima geração
def next_gen():
 #Função interna para contar o número de vizinhos vivos de uma célula
 def alive_neighbors(row, col):
  liveNeigh = 0
  for nr in range(-1, 2):
   for nc in range(-1, 2):
    if nr == nc == 0:
     continue
    r = row + nr
    c = col + nc
    if 0 <= r < rows and 0 <= c < cols:
     liveNeigh += board[r][c]
  return liveNeigh
 
 nextBoard = [[0 for _ in range(cols)] for _ in range(rows)]
 
 for row in range(rows):
  for col in range(cols):
   liveNeigh = alive_neighbors(row, col)
   if board[row][col]:
    if liveNeigh < 2 or liveNeigh > 3:
     continue
    else:
     nextBoard[row][col] = 1
   else:
    if liveNeigh == 3:
     nextBoard[row][col] = 1

 return nextBoard


#Função para imprimir o tabuleiro atual
def print_board(pboard):
 for i in range(rows):
  print("\n", pboard[i])

#Função que roda o jogo de acordo com a quantodade de gerações
def gameplay_loop():
 global board
 for g in range(1, gen + 1):
  time.sleep(1)
  board = next_gen()
  print("geração: ", g)
  print_board(board)


#"Main" do programa
rows = int(input("Insira a quantidade de linhas:    "))
cols = int(input("insira a quantidade de colunas:   "))
gen = int(input("insira quantas gerações terá o jogo:   "))

board = first_gen()
rows = len(board)
cols = len(board[0])
gameplay_loop()