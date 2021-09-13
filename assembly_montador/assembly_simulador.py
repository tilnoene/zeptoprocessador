def input_keyboard():
    instrucoes = []
    
    while True:
        try:
            linha = input()

            if linha == '' or linha[0] == '#':
                continue
            
            instrucoes.append(linha.split('#')[0].strip())
        except:
            break
    
    return instrucoes

def input_file(name='input.txt'):
    instrucoes = []

    arquivo = open(name, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        if linha == '\n' or linha[0] == '#':
            continue

        linha = linha.split('#')
        linha = linha[0].strip()

        instrucoes.append(linha.replace('\n', ''))

    return instrucoes

PC = 0
R = [0] * 16 # registradores
instrucoes = []
contador = 0

instrucoes = input_file()

# print(instrucoes)
while True:
    #print(PC, R)

    if contador > 3e5:
        break

    instrucao_atual = instrucoes[PC].split()
    reg = [int(e.replace('R', '')) for e in instrucao_atual[1].split(',')]
    
    if instrucao_atual[0] == 'addi':
        R[reg[0]] = R[reg[1]] + R[reg[2]] + reg[3]
        PC += 1
    elif instrucao_atual[0] == 'subi':
        R[reg[0]] = R[reg[1]] - R[reg[2]] - reg[3]
        PC += 1
    elif instrucao_atual[0] == 'andi':
        R[reg[0]] = R[reg[1]] & R[reg[2]] & reg[3]
        PC += 1
    elif instrucao_atual[0] == 'ori':
        R[reg[0]] = R[reg[1]] | R[reg[2]] | reg[3]
        PC += 1
    elif instrucao_atual[0] == 'xori':
        R[reg[0]] = R[reg[1]] ^ R[reg[2]] ^ reg[3]
        PC += 1
    elif instrucao_atual[0] == 'beq':
        if R[reg[0]] == R[reg[1]]:
            PC += reg[2]
        else:
            PC += 1
    elif instrucao_atual[0] == 'bleu': # sem sinal
        if abs(R[reg[0]]) <= abs(R[reg[1]]):
            PC += reg[2]
        else:
            PC += 1
    elif instrucao_atual[0] == 'bles': # com sinal
        if R[reg[0]] <= R[reg[1]]:
            PC += reg[2]
        else:
            PC += 1
    
    contador += 1

print(PC)     
print(R)