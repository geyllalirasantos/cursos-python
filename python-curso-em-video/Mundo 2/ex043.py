#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('-=' * 20)
print('CALCULADORA DE IMC')
print('-=' * 20)
peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura (ex: 1.68): '))

imc = peso / (altura * altura)
#outra opção do calculo imc: imc = peso * (altura ** 2)
print(f'Seu IMC é de {imc:.1f}.')

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'Você está com o PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Você está OBESO.')
else:
    print(f'Você está com OBESIDADE MÓRBIDA.')