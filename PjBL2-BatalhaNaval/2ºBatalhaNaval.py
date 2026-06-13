from rich.console import Console
console = Console(highlight=False)

#valores
l = 0
c = 0
embarcacao = 0
direcao = 0
string_alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# registros de ataque e navios
navios_j1 = {}
navios_j2 = {}
ataques_j1 = set()
ataques_j2 = set()
destruidos_j1 = []
destruidos_j2 = []

NAVIOS_INFO = {
    'P': ('Porta-avioes', 5),
    'E': ('Encouracado', 4),
    'C': ('Cruzador', 3),
    'S': ('Submarino', 3),
    'D': ('Destroyer', 2),
}

#define matriz A e B - completo
while True:
  tamanho_matriz = input("(min:10x10, max:26x26)\nQual o tamanho da matriz desejado?: ")
  if "x" not in tamanho_matriz:
    print("Formato invalido, deve ser (nnxnn)")
  else:
    novotamanho = tamanho_matriz.split("x",)
    linha_matriz = int(novotamanho[0])
    coluna_matriz = int(novotamanho[1])
    if linha_matriz > 26 or coluna_matriz > 26:
      print("Acima do tamanho maximo, insira outro tamanho")
    elif linha_matriz < 10 or coluna_matriz < 10:
      print("Abaixo do tamanho minimo, insira outro tamanho")
    else:
      break

#cria matrizes
matrizA = [["~"] * coluna_matriz for _ in range(linha_matriz)]
matrizB = [["~"] * coluna_matriz for _ in range(linha_matriz)]
matrizN = []

#cria string alfabeto
for i in range(len(matrizA)):
  matrizN.append(string_alfabeto[i])

#==================FUNÇÕES!!!==================
#print matrizes - completo
def print_matriz(matriz): 
  print("-  ",end="")
  for j in range(coluna_matriz):
    print(f"{str(j).rjust(2,' ')}   ",end="")
  print()
  for i in range(len(matriz)):
    console.print(string_alfabeto[i],f"[turquoise2]{matriz[i]}[/turquoise2]")
  print()

def print_ataque(matriz):
  print("-  ",end="")
  for j in range(coluna_matriz):
    print(f"{str(j).rjust(2,' ')}   ",end="")
  print()
  for i in range(linha_matriz):
    linha_display = []
    for j in range(coluna_matriz):
      cell = matriz[i][j]
      if cell == "[red]o[/red]" or cell == "[cyan]*[/cyan]":
        linha_display.append(cell)
      else:
        linha_display.append("~")
    console.print(string_alfabeto[i],f"[turquoise2]{linha_display}[/turquoise2]")
  print()

#validacao de bordas - completo
def valida_borda(lin,col,matriz):
  borda = len(matriz) -1
  if col > borda:
    col = 0
  elif col < 0:
    col = borda
  elif lin > borda:
    lin = 0
  elif lin < 0:
    lin = borda
  return lin,col

#valida embarcao e printa
def valida_embarcacao(embarcacao,tamanho,direcao,matriz,registro_navios):
  global l, c
  celulas = []
  if direcao == 'h':
    if tamanho+c > coluna_matriz:
      print("Embarcacao fora da matriz, insira em uma posicao valida.")
      return
    for i in range(tamanho):
      if matriz[l][c+i] != "~":
        print("Posicao ja ocupada, escolha outro local.")
        return
    for i in range(tamanho):
      matriz[l][c+i] = f'[white]{embarcacao}[/white]'
      celulas.append((l, c+i))

  elif direcao == 'v':
    if tamanho+l > linha_matriz:
      print("Embarcacao fora da matriz, insira em uma posicao valida.")
      return
    for i in range(tamanho):
      if matriz[l+i][c] != "~":
        print("Posicao ja ocupada, escolha outro local.")
        return
    for i in range(tamanho):
      matriz[l+i][c] = f'[white]{embarcacao}[/white]'
      celulas.append((l+i, c))
  nid = f"{embarcacao}{len(registro_navios)}"
  registro_navios[nid] = {
    'celulas': celulas,
    'nome': NAVIOS_INFO[embarcacao][0],
    'letra': embarcacao,
  }
  print("")

#seletor de embarcações
def embarcacoes(matriz, registro_navios):
  while True:
    print("1 - Porta-avioes 5\n2 - Encouracado 4\n3 - Cruzador 3\n4 - Submarino 3\n5 - Destroyer 2\n")
    embarcacao = input("Qual embarcacao deseja inserir? 0 para sair: ")
    print()
    direcao = input("(h ou v)\nQual direção?: ")
    print()
    match embarcacao:
      case '1':
        valida_embarcacao('P',5,direcao,matriz,registro_navios)
        print_matriz(matriz)
      case '2':
        valida_embarcacao('E',4,direcao,matriz,registro_navios)
        print_matriz(matriz)
      case '3':
        valida_embarcacao('C',3,direcao,matriz,registro_navios)
        print_matriz(matriz)
      case '4':
        valida_embarcacao('S',3,direcao,matriz,registro_navios)
        print_matriz(matriz)
      case '5':
        valida_embarcacao('D',2,direcao,matriz,registro_navios)
        print_matriz(matriz)
      case '0':
        cache_posicao = matriz[l][c]
        matriz[l][c] = "[yellow]+[/yellow]"
        print_matriz(matriz)
        matriz[l][c] = cache_posicao
        break
      case _:
        print("Opção inválida")

#valida se o navio foi totalemnte destruído
def checar_destruicao(pos, registro_navios, destruidos, ataques_set):
  for nid, info in registro_navios.items():
    if nid in destruidos:
      continue
    if pos in info['celulas']:
      if all(cp in ataques_set for cp in info['celulas']):
        destruidos.append(nid)
        return info['nome']
  return None

# interpretar uma coordenada digitada pelo jogador, organiza o texto recebido e verifica se a letra e o número que foi informado existe dentro da matiz e se estiver certo vai converter a coordenada para a posição na matriz.
# caso  a coordenada seja inválida a retorn None indica que a entrada não corresponde e matriz.
def pase_coordenada(entrada):
  entrada = entrada.strip().upper().replace(" ","")
  if len(entrada) < 2:
    return None
  letra = entrada[0]
  if letra not in string_alfabeto[:linha_matriz]:
    return None
  try:
    col = int(entrada[1:])
  except ValueError:
    return None
  if col < 0 or col >= coluna_matriz:
    return None
  return string_alfabeto.index(letra), col

#controla o ataque. primeiro o jogador informa a posição o código verifica se a posição é válida e se já foi atacada. depois o código analiza se o ataque atingiu a embarcação
#se acertar, a posição é marcada como atingita e verifica se o navio foi completamente destuído. caso contrário, a jogada é registrada como tiro na água
def realizar_ataque(matriz_alvo, registro_alvo, destruidos_alvo, ataques_set, nome_jogador):
  while True:
    entrada = input(f"{nome_jogador}, informe a coordenada do ataque (ex: A5): ").strip()
    coord = pase_coordenada(entrada)
    if coord is None:
      print("Coordenada invalida. Use letra + numero, ex: B3")
      continue
    lin, col = coord
    if (lin, col) in ataques_set:
      print("Voce ja atacou essa posicao! Escolha outra.")
      continue
    ataques_set.add((lin, col))
    acertou = any((lin, col) in info['celulas'] for info in registro_alvo.values())
    if acertou:
      matriz_alvo[lin][col] = "[red]o[/red]"
      print(f"ACERTO em {string_alfabeto[lin]}{col}!")
      destruido = checar_destruicao((lin, col), registro_alvo, destruidos_alvo, ataques_set)
      if destruido:
        print(f"{destruido} DESTRUIDO!")
    else:
      matriz_alvo[lin][col] = "[cyan]*[/cyan]"
      print(f"Agua em {string_alfabeto[lin]}{col}.")
    break

# verifica se as embarcações do jogador foram destruídos, compara os navios registrados com os navios com os destruídos. se todos foram destruídos. se foram destruidos volta true 
# se não retorna false, assim verificaa se a vencedores.
def todos_destruidos(registro, destruidos):
  return len(destruidos) >= len(registro) and len(registro) > 0
# mostra o placar no andamento da partida
def mostrar_placar(nome_j1, nome_j2):
  print("\n== PLACAR ==")
  print(f"Navios de {nome_j2} destruidos: {len(destruidos_j1)}/{len(navios_j2)}")
  for nid in destruidos_j1:
    print(f"  + {navios_j2[nid]['nome']}")
  print(f"Navios de {nome_j1} destruidos: {len(destruidos_j2)}/{len(navios_j1)}")
  for nid in destruidos_j2:
    print(f"  + {navios_j1[nid]['nome']}")
  print()

# controla a troca de turnos 
# solicita que o controle seja passado ao próximo jogador antes de continuar a partida. 
# o código pede os nomes dos dois jogadores para identificar durante o jogo.
def passar_vez(proximo):
  input(f"\nPasse o controle para {proximo} e pressione Enter...")
  print("\n" * 40)
nome_j1 = input("Nome do Jogador 1: ").strip() or "Jogador 1"
nome_j2 = input("Nome do Jogador 2: ").strip() or "Jogador 2"
print()

#interface_grafica
def interface_grafica(jogador,matriz,navios_j):
  global l,c
  print(f"== {jogador}: posicione seus navios ==")
  print_matriz(matriz)
  while True:
    seletor = input("Enter para por uma embarcacao\nWASD para mover, 0 para sair: ")
    print()
    match seletor:
      case "w"|"W":
        l-=1
        l, c = valida_borda(l,c,matriz)
        cache_posicao = matriz[l][c]
        matriz[l][c] = "[yellow]+[/yellow]"
        print_matriz(matriz)
        matriz[l][c] = cache_posicao
      case "s"|"S":
        l+=1
        l, c = valida_borda(l,c,matriz)
        cache_posicao = matriz[l][c]
        matriz[l][c] = "[yellow]+[/yellow]"
        print_matriz(matriz)
        matriz[l][c] = cache_posicao
      case "a"|"A":
        c -=1
        l, c = valida_borda(l,c,matriz)
        cache_posicao = matriz[l][c]
        matriz[l][c] = "[yellow]+[/yellow]"
        print_matriz(matriz)
        matriz[l][c] = cache_posicao
      case "d"|"D":
        c +=1
        l, c = valida_borda(l,c,matriz)
        cache_posicao = matriz[l][c]
        matriz[l][c] = "[yellow]+[/yellow]"
        print_matriz(matriz)
        matriz[l][c] = cache_posicao
      case "":
        if matriz == matrizA:
          embarcacoes(matriz, navios_j)
        elif matriz == matrizB:
          embarcacoes(matriz, navios_j)
      case "0":
        break
      case _:
        print("Opção inválida")
  
interface_grafica(nome_j1,matrizA,navios_j1)

# posicionamento jogador 2
passar_vez(nome_j2)
l, c = 0, 0
interface_grafica(nome_j2,matrizB,navios_j2)

# while partidas
#controla a partida . os jogadores revezam os turnos, realizando ataques contra os navios do adversário. 
#Depois de cada ataque, o placar é atualizado e o código verifica se todos os navios do outro jogador já foram destruídos. 
#Quando isso acontece, um jogador é declarado vencedor e a partida é encerrada.
passar_vez(nome_j1)
print("\n== BATALHA INICIADA! ==\n")

while True:
  print(f"Turno de {nome_j1} -- grade inimiga:")
  print_ataque(matrizB)
  realizar_ataque(matrizB, navios_j2, destruidos_j1, ataques_j1, nome_j1)
  mostrar_placar(nome_j1, nome_j2)

  if todos_destruidos(navios_j2, destruidos_j1):
    print(f"{nome_j1} VENCEU! Todos os navios de {nome_j2} foram destruidos!")
    break

  passar_vez(nome_j2)
  print(f"Turno de {nome_j2} -- grade inimiga:")
  print_ataque(matrizA)
  realizar_ataque(matrizA, navios_j1, destruidos_j2, ataques_j2, nome_j2)
  mostrar_placar(nome_j1, nome_j2)

  if todos_destruidos(navios_j1, destruidos_j2):
    print(f"{nome_j2} VENCEU! Todos os navios de {nome_j1} foram destruidos!")
    break

  passar_vez(nome_j1)
