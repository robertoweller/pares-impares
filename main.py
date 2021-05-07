"""
Pares e Ímpares
Faça um programa que leia um arquivo texto contendo uma lista de número
inteiros separados por "\n" e gere dois outros arquivos, um contendo
os números pares e o outros os números ímpares. No programa principal
deve ser lido um arquivo de entrada e deve ser chamada função que receba
uma lista contendo cada linha do arquivo e entrada. Esta função deve criar
duas listas, uma contendo os números pares e outra contendo os números ímpares.
Ao final, cada lista deve ser armazenada em um arquivo onde cada número deve 
estar separado por ",".

Exemplos:

Arquivo de entrada:
------------------------
200
197
564
351
765
466
17
------------------------


Arquivos de saída:
---------------------------------------------------
200,564,466            | 197,351,765,17           |
                       |                          |
                       |                          |
                       |                          |
                       |                          |
---------------------------------------------------

Saída:
-----------------------------------------------------
Dígite o nome do arquivo: inteiros.txt

Arquivos pares.txt e impares.txt criados com sucesso!
-----------------------------------------------------

"""

def recebeArquivo(res):
    
    pares = []
    impares = []
    res = list(map(int, ''.join(res).split()))
    for n in res:
   
        if n % 2 == 0:
            pares.append(n)
            
        else:
            impares.append(n)

    impar = open('impares.txt', 'w')
    par = open('pares.txt', 'w')

    par.write(','.join(map(str, pares)))
    impar.write(','.join(map(str, impares)))
    
    impar.close()
    par.close()
 
    print('\nArquivos pares.txt e impares.txt criados com sucesso!')



if __name__ == '__main__':
    resposta = input('Dígite o nome do arquivo: ')
    try:
        with open(resposta, 'r') as arq:
            recebeArquivo(arq)
    except FileNotFoundError:
        print('\nEsse arquivo não foi encontrado!')
