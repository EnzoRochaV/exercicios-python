for i in range(2):
    print()
    p = float(input('Qual o seu peso ? '))
    print()
    h= float(input('Qual a sua altura? '))
    print()
    imc=round(p/(h)**2, 2)
    if imc <= 18.5:
        print(f'seu IMC é {imc}, entao vc esta abaixo do peso ideal')
    elif imc <= 24.9:
        print(f'seu IMC é {imc}, entao vc esta no seu peso ideal')
    elif imc <= 29.9:
        print(f'seu IMC é {imc}, entao vc esta com sobrepeso')
    elif imc <= 34.9:
        print(f'seu IMC é {imc}, entao vc esta com obesidade grau 1')
    elif imc <= 39.9:
        print(f'seu IMC é {imc}, entao vc esta com obesidade grau 2')
    elif imc>= 40:
        print(f'seu IMC é {imc}, entao vc esta com obesidade grau 3')    
    else:
        print('ola')