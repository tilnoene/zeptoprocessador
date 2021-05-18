for X in range(0, 257):
    for Y in range(0, 257):
        PC = 0
        R = [0] * 16 # registradores
        instrucoes = ['addi R1,R0,0,0', f'addi R2,R0,R0,{X}', f'addi R3,R0,R0,{Y}', 'addi R4,R0,R0,0', 'beq R3,R4,4', 'addi R1,R1,R2,0', 'addi R4,R4,R0,1', 'beq R0,R0,-3', 'beq R1,R1,0']
        contador = 0
        
        while PC < len(instrucoes):
            if contador > 4096:
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

        if R[1] != X*Y:
            print(f'ERRO EM {X} * {Y}. Obtido: {R[1]}, Esperado: {X*Y}')