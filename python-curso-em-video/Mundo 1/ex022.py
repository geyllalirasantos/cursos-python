#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

name = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome... ')
print(f'O seu nome completo em LETRAS MAIÚSCULAS É: {name.upper()} \n'
      f'O seu nome completo em letras minusculas é: {name.lower()} \n'
      f'O seu nome completo sem espaços tem {len(name) - name.count(" ")} letras')
#print(f'\nO seu primeiro nome tem {name.find(" ")} letras')

separa = name.split()
print(f'Seu nprimeiro nome tem {len(separa[0])} letras')