from rich import print
from random import randint

#valores
l = 0
c = 0
string_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
marca_X = "[bright_red]X[/bright_red]"
marca_x = "[orange1]X[/orange1]"

#cria matriz A
tamanho_matriz = input("Qual o tamanho da matriz desejado?: (min:10x10, max:26x26)")
novotamanho = tamanho_matriz.split("x",)
linha_matriz = int(novotamanho[0])
coluna_matriz = int(novotamanho[1])
matrizA = [["~"] * coluna_matriz for _ in range(linha_matriz)]
matrizN = []
#cria string alfabeto
for i in range(len(matrizA)):
  matrizN.append(string_alfabeto[i])

#print matriz A
def printA():
  print("-  ",end="")
  for j in range(coluna_matriz): #printa a primeira linha de números
    print(f"[bright_white]{str(j).rjust(2," ")}   [/bright_white]",end="")
  print()

  for i in range(len(matrizA)):
    print(string_alfabeto[i],f"[turquoise2]{matrizA[i]}[/turquoise2]")
  print()

#validação de bordas
def valida_borda(a,b):
  borda = len(matrizA) -1
  if b > borda:
    b = 0
  elif b < 0:
    b = borda
  elif a > borda:
    a = 0
  elif a < 0:
    a = borda
  return a,b

'''
def embarcacoes():
  for j in range(linha_matriz):
    for i in range(coluna_matriz):
      if matrizAA[j][i] == "~":
        matrizAA[j][i] = "~" #agua
      elif matrizAA[j][i] == "x":
        matrizAA[j][i] = "[orange1]X[/orange1]" #acerto
      elif matrizAA[j][i] == "X":
        matrizAA[j][i] = marca_X
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X      
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X
      elif matrizAA[j][i] == 0:
        matrizAA[j][i] = marca_X

agua = ~
acerto = x
marcaX = X
navio destruido = 0


Porta-aviões 	5  = P
Encouraçado 	4  = E
Cruzador 	3  = C 
Submarino 	3 = S 
Destroyer 	2 = D
'''

#move o seletor (x) na matriz
printA()
while True:
  seletor = input("WASD para mover, 0 para sair: ")
  match seletor:
    case "w"|"W":
      l-=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = marca_x
      printA()
      matrizA[l][c] = cache_posicao
    case "s"|"S":
      l+=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = marca_X
      printA()
      matrizA[l][c] = cache_posicao
    case "a"|"A":
      c -=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = marca_X
      printA()
      matrizA[l][c] = cache_posicao
    case "d"|"D":
      c +=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = marca_X
      printA()
      matrizA[l][c] = cache_posicao
    case "":
      print("Enter")
    case "0":
      break
    case _:
      print("opção invalida")
