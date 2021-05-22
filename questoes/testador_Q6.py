from random import randint

limites = [(1, 65535), (65535, 1), (65535, 65535), (1, 1), (65535, 2), (2, 65535), (2, 1), (1, 2), (13271, 7), (7, 13271)]

for i in range(0, 10):
    X = Y = 1

    if i < len(limites):
        X = limites[i][0]
        Y = limites[i][1]
    else:
        X = randint(1, 65536)
        Y = randint(1, 65536)
            
    PC = 0
    R = [0] * 16 # registradores
    instrucoes = ['addi R1,R0,0,0', f'addi R2,R0,R0,{X}', f'addi R3,R0,R0,{Y}', 'bles R2,R0,3', 'subi R2,R2,R3,0', 'beq R0,R0,-2', 'addi R1,R2,R0,0', 'bles R0,R1,2', 'addi R1,R1,R3,0', 'beq R1,R1,0']
    contador = 0
        
    while True:
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

    resto = X % Y
    if resto < 0:
        resto += Y

    if R[1] != resto:
        print(f'ERRO EM {X} % {Y}. Obtido: {R[1]}, Esperado: {resto}')