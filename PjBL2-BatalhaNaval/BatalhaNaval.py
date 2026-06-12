from random import randint
from rich.console import Console
console = Console(highlight=False)

#valores
l = 0
c = 0
embarcacao = 0
direcao = 0
string_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
marca_x = "[orange1]X[/orange1]"

#cria matriz A e B 
while True:
  tamanho_matriz = input("(min:10x10, max:26x26)\nQual o tamanho da matriz desejado?: ")
  if "x" not in tamanho_matriz:
    print("Formato inválido, deve ser (nnxnn)")
  else:
    novotamanho = tamanho_matriz.split("x",)
    linha_matriz = int(novotamanho[0])
    coluna_matriz = int(novotamanho[1])
    if linha_matriz > 26 or coluna_matriz > 26:
      print("Acima do tamanho máximo, insira outro tamanho")
    elif linha_matriz < 10 or coluna_matriz < 10:
      print("Abaixo do tamanho mínimo, insira outro tamanho")
    else:
      break
matrizA = [["~"] * coluna_matriz for _ in range(linha_matriz)]
matrizB = [["~"] * coluna_matriz for _ in range(linha_matriz)]
matrizN = []

#cria string alfabeto
for i in range(len(matrizA)):
  matrizN.append(string_alfabeto[i])

#print matriz A
def printA():
  print("-  ",end="")
  for j in range(coluna_matriz): #printa a primeira linha de números
    print(f"{str(j).rjust(2," ")}   ",end="")
  print()

  for i in range(len(matrizA)):
    console.print(string_alfabeto[i],f"[turquoise2]{matrizA[i]}[/turquoise2]")
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

def valida_embarcacao(e,t,d):
  if d == 'h':
    if t+c > coluna_matriz:
      print("Embarcação fora da matriz, insira em uma posição válida.")
    else:
      for i in range(t):
        matrizA[l][c+i] = f'[white]{e}[/white]'
  elif d == 'v':
    if t+l > linha_matriz:
      print("Embarcação fora da matriz, insira em uma posição válida.")
    else:
      for i in range(t):
        matrizA[l+i][c] = f'[white]{e}[/white]'
  print("")

def embarcacoes():
  while True:
    print("1 - Porta-aviões 5\n2 - Encouraçado 4\n3 - Cruzador 3\n4 - Submarino 3\n5 - Destroyer 2\n")
    embarcacao = input("Qual embarcação deseja inserir? 0 para sair: ")
    print()
    match embarcacao:
      case '1':
        valida_embarcacao('P',5,'v')
        printA()
      case '2':
        valida_embarcacao('E',4,'v')
        printA()
      case '3':
        valida_embarcacao('C',3,'v')
        printA()
      case '4':
        valida_embarcacao('S',3,'v')
        printA()
      case '5':
        valida_embarcacao('D',2,'v')
        printA()
      case '0':
        cache_posicao = matrizA[l][c]
        matrizA[l][c] = "[yellow]+[/yellow]"  
        printA()
        matrizA[l][c] = cache_posicao
        break
      case _:
        print("Opção inválida")


#move o seletor (x) na matriz
printA()
while True:
  seletor = input("Enter para por uma embarcação\nWASD para mover, 0 para sair: ")
  print()
  match seletor:
    case "w"|"W":
      l-=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = "[yellow]+[/yellow]"
      printA()
      matrizA[l][c] = cache_posicao
    case "s"|"S":
      l+=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = "[yellow]+[/yellow]"
      printA()
      matrizA[l][c] = cache_posicao
    case "a"|"A":
      c -=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = "[yellow]+[/yellow]"
      printA()
      matrizA[l][c] = cache_posicao
    case "d"|"D":
      c +=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = "[yellow]+[/yellow]"
      printA()
      matrizA[l][c] = cache_posicao
    case "":
      embarcacoes()
    case "0":
      break
    case _:
      print("Opção inválida")
