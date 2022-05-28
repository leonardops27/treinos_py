print('''
        Brincando com listas e loops!!!
        Cada número escolhido substitui o 
        número impresso por "x" .
        ''')
a = [[1],  [2],  [3]]
b = [[4],  [5],  [6]]
c = [[7],  [8],  [9]]
O = a,b,c

while True:
    for x in O:
        print (' '*10, x)
    print()
    mudança = int(input('      Escolha o número("0" Sair): '))
    if mudança == 0:
        print(' '*5,'='*3,'Até uma outra vez!!!','='*3)
        break
    if mudança == 1:
        O[0][0] = 'x'
    if mudança == 2:
        O[0][1] = 'x'
    if mudança == 3:
        O[0][2] = 'x'
    if mudança == 4:
        O[1][0] = 'x'
    if mudança == 5:
        O[1][1] = 'x'
    if mudança == 6:
        O[1][2] = 'x'
    if mudança == 7:
        O[2][0] = 'x'
    if mudança == 8:
        O[2][1] = 'x'
    if mudança == 9:
        O[2][2] = 'x'


