'''
Lucas encontrou um celular muito antigo na sua casa, trata-se de um Nokia 1100. Foi o primeiro celular que 
ele teve, então bateu aquela nostalgia. Para sua surpresa, o celular ainda estava funcionando e, logo após 
ele relembrar como era jogar Snake e Space Impact, ele decidiu relembrar também como era digitar uma mensagem 
naquele modelo de teclado.

Caso você não lembre, os teclados dos celulares mais antigos não eram no padrão QWERTY, mas alfanumérico. 
Esse tipo de teclado foi adotado no início da era digital dos celulares, quando a Internet ainda não tinha 
a mesma presença que tem hoje nestes aparelhos. Nele cada uma das teclas numéricas comuns equivale a mais de 
uma letra ou sinal do alfabeto.

A letra 'c', por exemplo, é a terceira letra contida na tecla 2. Sendo assim, em uma mensagem de texto, para 
digitar o letra ‘c’, você precisaria pressionar a tecla 2 por 3 vezes (em um intervalo de tempo curto). Para letras maiúsculas, você precisava pressionar a tecla # e, em seguida, digitar a letra desejada.

Os símbolos, por sua vez, estão presentes na tecla _; portanto, para digitar os símbolos '_', '.', '!' e '?', 
você precisaria pressionar a tecla * por 1, 2, 3 ou 4 vezes, respectivamente. Por fim, o espaço pode ser digitado 
apenas pressionando a tecla 0 uma única vez.

Sabendo disso, sua missão será criar um código que, dada uma mensagem, terá que informar quais teclas e quantas 
vezes cada tecla deverá ser pressionada para que a mensagem do Lucas seja digitada corretamente no seu Nokia 1100.

Entrada
Seu programa vai receber uma string M com N caracteres ($0 < N < 1000$) que representa a mensagem que o Lucas 
deseja digitar no seu celular. Essa mensagem poderá conter espaços, letras maiúsculas e minúsculas (a-z e A-Z), 
sem acentuação, e os caracteres '.', '!' e '?'.

Saída
A saída do programa será composta por N linhas ou mais. Cada linha representará a tecla que deverá ser 
pressionada para gerar o caractere presente na mensagem. Por exemplo, se a mensagem for 'hi', seu programa 
deverá exibir 2 linhas na saída: a primeira será 4 - 2 vez(es), e a segunda será 4 - 3 vez(es), visto que 
será necessário pressionar a tecla 4 duas vezes e, em seguida, a tecla 4 três vezes.

Considere que qualquer letra maiúscula exige que o Lucas pressione a tecla # antes de digitá-la.
'''

def keyboard(message):
    import string
    board = ['abc', 'def', 'ghi', 'jkl', 
    'mno', 'pqrs', 'tuv', 'wxyz']

    simbols = '_.!?'

    out = []

    for letter in message:
        if letter in string.ascii_uppercase:
            out.append('# - 1 vez(es)')
            for pos, num in enumerate(board):
                if letter.lower() in num:
                    out.append(f'{pos + 2} - {num.index(letter.lower())+1} vez(es)')
        elif letter == ' ':
            out.append('0 - 1 vez(es)')
        elif letter in simbols:
            out.append(f'* - {simbols.index(letter)+1} vez(es)')
        
        for pos, num in enumerate(board):
            if letter in num:
                out.append(f'{pos + 2} - {num.index(letter)+1} vez(es)') 
    
    return out