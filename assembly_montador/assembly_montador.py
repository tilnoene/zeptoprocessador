opcodes = {
    'addi': '0000',
    'subi': '0001',
    'andi': '0010',
    'ori': '0011',
    'xori': '0100',
    'beq': '0101',
    'bleu': '0110',
    'bles': '0111'
}

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
        linha = linha.split('#')
        linha = linha[0].strip()

        instrucoes.append(linha.replace('\n', ''))

    return instrucoes

def write_memory(name, content):
    content += (4096 - len(content)) * ['FFFF'] # preenche o resto da memória

    linhas = []
    for i in range(0, len(content), 8):
        linhas.append([' '.join(content[i:i+8]) + '\n'])

    arquivo = open(name, 'w')
    arquivo.write('#A 0000h\n#H\n\n')

    for linha in linhas:
        arquivo.writelines(linha)
    arquivo.close()

def convert_hex(number):
    converted_number = ''

    for i in range(0, len(number), 4):
        converted_number += hex(int(number[i:i+4], 2)).split('x')[1].upper()

    return converted_number

def main():
    instrucoes = input_file() # input_keyboard() ou input_file()
    
    mem1 = [] # instruções
    mem2 = [] # imediatos
    
    for instrucao in instrucoes:
        if instrucao == '' or instrucao[0] == '#':
            continue
            
        instrucao = instrucao.split()

        opcode = hex(int(opcodes[instrucao[0]], 2)).split('x')[1]
        valores = [e.replace('R', '') for e in instrucao[1].split(',')]

        if instrucao[0] in ['beq', 'bleu', 'bles']:
            # Ra Rb Opcode
            rd = '0'
            ra = hex(int(valores[0])).split('x')[1]
            rb = hex(int(valores[1])).split('x')[1]

            mem2.append(rd + ra + rb + opcode)
        else:
            # Rd Ra Rb Opcode
            rd = hex(int(valores[0])).split('x')[1]
            ra = hex(int(valores[1])).split('x')[1]
            rb = hex(int(valores[2])).split('x')[1]
            
            mem2.append(rd + ra + rb + opcode)
            
        imm = int(valores[-1])
        binary_number = str(bin(imm)).split('b')[1]

        if imm < 0: # complemento de 2
            binary_number = bin((-1)*(65535 + 1 - abs(imm)))

            imm = binary_number.split('b')[1]
        else:
            binary_number = str(binary_number)

            imm = binary_number.rjust(16, '0') # extensão de sinal
        
        imm = convert_hex(imm)
        mem1.append(imm)

    write_memory('mem1.drs', mem1)
    write_memory('mem2.drs', mem2)
    
main()