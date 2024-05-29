vc = float(input("Qual foi o valor da compra? "))
print()
print('certo, qual a forma de pagamento? ')
print()
pg = input('escolha entre: a vista, 2 vezes ou 3 vezes. ')
print()


if pg == 'a vista':
    valor = vc -(vc * 0.1)
    valor = round(valor,2)
    print()
    print(f'valor total com 10% de desconto igual a {valor} reais')
elif pg == '2':
    valor = vc/2
    valor = round(valor,2)
    print()
    print(f'no total ficaram 2 parcelas de {valor} reais')
elif pg == '3':
    juros = vc * 0.1
    valor = vc/3 + juros
    valor = round(valor,2)
    print()
    print(f'no total ficaram 3 parcelas de {valor} reais')
else :
    print()
    print('valor nao aceito')
