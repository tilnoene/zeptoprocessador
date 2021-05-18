<h2>💬 Sobre o projeto</h2>

Projeto e implementação de um processador de 16 bits utilizando o software simulador <a href="https://www.digitalelectronicsdeeds.com/deeds.html" target="_blank">Deeds</a>. Projeto final da disciplina Laboratório de Circuitos Lógicos da Universidade de Brasília.

<h2>🛠 Como utilizar</h2>

### Processador

Foi implementado na versão 2.40.330 (Jan 07, 2021) do software <a href="https://www.digitalelectronicsdeeds.com/deeds.html" target="_blank">Deeds</a>.

O arquivo principal é o `processador.pbs`, que interliga todos os outros componentes. Ao clicar a tecla F9 a simulação é iniciada, o sinal de reset recebe um pulso automaticamente e limpa todos os registradores. Ao clicar `Ctrl + K` o clock automático é ativado e as instruções são executadas. É possível ver os valores dos registradores, endereços e demais estados nos respectivos displays de 7 segmentos.

Cada arquivo na pasta principal é um componente do processador, usado para diminuir o circuito e facilitar a implementação. Cada componente pode ser testado avulsamente com seu respecitvo arquivo na pasta `teste_bloco_de_circuito`.

### Compilador

Compila as instruções em Assembly para as duas memórias utilizadas pelo processador.

1. No arquivo `input.txt` escreva o código em Assembly (de acordo com a tabela de instruções).
2. Execute o arquivo `assembly_compiler.py`.
3. Serão gerados dois arquivos `mem1.drs` e `mem2.drs` contendo o conteúdo de cada memória, respectivamente (o primeiro contém os imediatos e o segundo contém a instrução em si).

Observações:

- Não escreva espaços após as vírgulas
- Comentários apenas no final da linha de uma instrução ou em linhas separadas (exemplo: `addi R1,R0,R0,16 # R1=16`)

### Simulador das instruções do processador

Simula o código em assembly, sem a necessidade de executar no processador pelo simulador.

1. No arquivo `input.txt` escreva o código em Assembly (de acordo com a tabela de instruções).
2. Execute o arquivo `assembly_simulator.py`
3. No terminal aparecerá o valor do registrador PC na primeira linha e os valores dos outros 16 registradores na linha seguinte.

Você pode verificar os valores dos registradores após cada etapa a linha 44 do código (diminua o limite de instruções na condição do `if` na linha 46).

<h2>⚙️ Especificações Técnicas</h2>

O processador possui duas memórias capaz de armazenar 4096 instruções de 16 bits cada. A primeira memória contém os 16 bits menos significativos da instrução e a segunda memória contem os 16 bits mais significativos (imediato).

Cada instrução tem 32 bits de tamanho codificados com os seguintes campos:

<table>
  <tr>
    <td>15</td>
    <td>14</td>
    <td>13</td>
    <td>12</td>
    <td>11</td>
    <td>10</td>
    <td>9</td>
    <td>8</td>
    <td>7</td>
    <td>6</td>
    <td>5</td>
    <td>4</td>
    <td>3</td>
    <td>2</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td colspan="4" style="text-align:center;"><b>Rd</b></td>
    <td colspan="4" style="text-align:center;"><b>Ra</b></td>
    <td colspan="4" style="text-align:center;"><b>Rb</b></td>
    <td colspan="4" style="text-align:center;"><b>Opcode</b></td>
  </tr>
</table>

<table>
  <tr>
    <td>31</td>
    <td>30</td>
    <td>29</td>
    <td>28</td>
    <td>27</td>
    <td>26</td>
    <td>25</td>
    <td>24</td>
    <td>23</td>
    <td>22</td>
    <td>21</td>
    <td>20</td>
    <td>19</td>
    <td>18</td>
    <td>17</td>
    <td>16</td>
  </tr>
  <tr>
    <td colspan="16" style="text-align:center;"><b>Imediato</b></td>
  </tr>
</table>

## Instruções
| Opcode |       Mnemônico      |                  Nome                  |                    Operação                 |
|:------:|:--------------------:|:--------------------------------------:|:-------------------------------------------:|
|  0000  | addi Rd, Ra, Rb, Imm |            Soma com imediato           |              Rd = Ra + Rb + Imm             |
|  0001  | subi Rd, Ra, Rb, Imm |         Subtração com imediato         |              Rd = Ra - Rb - Imm             |
|  0010  | andi Rd, Ra, Rb, Imm |        AND bitwise com imediato        |              Rd = Ra & Rb & Imm             |
|  0011  |  ori Rd, Ra, Rb, Imm |         OR bitwise com imediato        |              Rd = Ra | Rb | Imm             |
|  0100  | xori Rd, Ra, Rb, Imm |        XOR bitwise com imediato        |            Ra = Ra xor Rb xor Imm           |
|  0101  |    beq Ra, Rb, Imm   |             Salto se igual             |         Ra==Rb ? PC=PC+Imm : PC=PC+1        |
|  0110  |   bleu Ra, Rb, Imm   | Salto se menor ou igual<br>(sem sinal) | Ra<=Rb ? PC=PC+Imm : PC=PC+1<br>(sem sinal) |
|  0111  |   bles Ra, Rb, Imm   | Salto se menor ou igual<br>(com sinal) | Ra<=Rb ? PC=PC+Imm : PC=PC+1<br>(com sinal) |

# Markdown syntax guide

## Headers

# This is a Heading h1
## This is a Heading h2 
###### This is a Heading h6

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is a alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight tamarkup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.