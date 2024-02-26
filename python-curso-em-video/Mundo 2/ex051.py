#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmética: '))

#para saber o decimo termo da pa
decimo = t + (10 -1) * r

for c in range(t, decimo + r, r):
    print(c, end=' -> ')
print('FIM')