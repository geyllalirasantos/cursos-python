#Aprimore o desafio anterior, mostrando no final:                                                    
# - A soma de todos os valores pares digitados.                                                                                                  
# - A soma dos valores da terceira coluna.                                                                                                                
# - O maior valor da segunda linha.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

somapar = 0
somacoluna = 0
maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' * 40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-' * 40)

#implementação a partir daqui
#soma dos valores pares da matriz
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
print(f'A soma dos valores pares é {somapar}')

#soma dos valores da terceira coluna
for l in range(0,3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')

#o maior valor da segunda linha
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')