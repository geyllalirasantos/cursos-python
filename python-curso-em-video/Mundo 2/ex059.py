#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    print('  [1] somar\n'
         '  [2] multiplicar\n'
         '  [3] maior\n'
         '  [4] novos números\n'
         '  [5] sair do programa')
    escolha = int(input('>>>>>>> Qual é a sua opção? '))

    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
        #print('-' * 30)
    elif escolha == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
        #print('-' * 30)
    elif escolha == 3:
        if n1 < n2:
            maior = n1
           #print('-' * 30)
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
            #print('-' * 30)
    elif escolha == 4:
        print('-' * 30)
        print('Inserindo novos valores...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando o programa')
    else:
        print('Opção inválida. Tente novamente.')
    print('-' * 30)
print('Fim do programa!')