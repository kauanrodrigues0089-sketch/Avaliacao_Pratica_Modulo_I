#Kauan Pietro Santos Rodrigues
peso = float(input('digite seu peso (kg)'))
altura = float(input('digite sua altura (m)'))

IMC = peso / (altura * altura)
print(f'seu imc e:{IMC:.2f}')
if  IMC < 18.5:
    print('abaixo do peso')
elif IMC <24.9:
    print('peso normal')
elif IMC <29.9:
    print('sobrepeso')
elif IMC < 34.9:
    print('obesidade grau I')
elif IMC <39.9:
    print('obesidade grau II')
else:
    print('obesidade grau III(morbida)')