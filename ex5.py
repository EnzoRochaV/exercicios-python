print()
n = int(input('Digite um numero para obter sua tabada  '))
m = 1
print()
while m <= 10 :
    t = n*m
    if m < 10:
        if t < 10:
            print(f'{n} X  {m} =  {t}')
        else:
            print(f'{n} X  {m} = {t}')
    else:
        print(f'{n} X {m} = {t}')
    m = m + 1
