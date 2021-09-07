altura = float(input('Qual é a sua altura em cm'))
peso = float(input('Qual é o seu peso em kg:'))

IMC  = peso / (altura/100)**2

print (IMC)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC}, e é classificado como magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {IMC}, e é considerado normal')

elif IMC >= 25 and IMC < 24.9:
    print(f'Seu IMC é de {IMC}, e é classificado como sobrepeso. Pouco, mas fica o alerta!')

elif IMC >= 30 and IMC < 39.9:
    print(f'Seu IMC é de {IMC}, e é classificado como obesidade, fique atento e mude seus habitos!')

else:
    print ( "Comece a se alimentar melhor e se exercitar, obesidade grave!")