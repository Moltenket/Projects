from rich import print

#valores
l = 0
c = 0
z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
marca_X = "[bright_red]X[/bright_red]"

#cria matrizes
tamanho_matriz = input("Qual o tamanho da matriz desejado?: (min:10x10, max:26x26)")
novotamanho = tamanho_matriz.split("x")
largura_matriz = int(novotamanho[0])
coluna_matriz = int(novotamanho[1])

matrizA = [["~"] * largura_matriz for _ in range(coluna_matriz)]
matrizN = []
for i in range(len(matrizA)):
  matrizN.append(z[i])

def printA():
  #print(f"0 {matrizN}")
  print("[bright_white]-\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9[/bright_white]")
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
