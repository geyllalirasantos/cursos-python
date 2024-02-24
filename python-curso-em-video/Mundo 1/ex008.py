#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m=float(input('Uma distância em metros: '))
cm=m*100
mm=m*1000
print(f'A medida de {m}m equivalem a {cm:.0f} centímetros e {mm:.0f} milímetros')


'''
aprimoramento do desafio com todas as conversões
km=m/1000
hm=m/100
dam=m/10
dm=m*10
print(f'A medida de {m}m corresponde a: \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f} \n{mm:.0f}mm')
'''