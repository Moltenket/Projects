from rich import print

#valores
l = 0
c = 0
marca_X = "[bright_red]X[/bright_red]"
z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#cria matrizes
tamanho_matriz = int(input("Qual o tamanho da matriz desejado?: (min:10x10, max:26x26)"))
matrizA = [["~"] * tamanho_matriz for _ in range(tamanho_matriz)]
matrizN = []
for i in range(len(matrizA)):
  matrizN.append(z[i])

def printA():
  #print(f"0 {matrizN}")
  print("[bright_white]-   0    1    2    3    4    5    6    7    8    9[/bright_white]")
  for i in range(len(matrizA)):
    print(z[i],f"[turquoise2]{matrizA[i]}[/turquoise2]")
  print()
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

printA()
while True:
  seletor = input("WASD para mover, 0 para sair: ")
  match seletor:
    case "w"|"W":
      l-=1
      l, c = valida_borda(l,c)
      cache_posicao = matrizA[l][c]
      matrizA[l][c] = marca_X
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
    case "0":
      break
    case _:
      print("opção invalida")
