x= int(input("Nota 1 : "))

p1=4

y= int(input("Nota 2 : "))

p2=5

z= int(input("Nota 3 : "))

p3=2

t=((x*p1)+(y*p2)+(z*p3)) / (p1+p2+p3)

media=round(t,2)

if t > 5:
    print(f'Sendo nota 1 = {x} com peso = {p1}, nota 2 = {y} com peso = {p2}, e nota 3 = {z} com peso = {p3}, o valor da media final é = {media}. Portanto, você passou de ano')
    
elif t == 5:
    print(f'Sendo nota 1 = {x} com peso = {p1}, nota 2 = {y} com peso = {p2}, e nota 3 = {z} com peso = {p3}, o valor da media final é = {media}. Portanto, você esta na média e passou de ano')
    
else:
    print(f'Sendo nota 1 = {x} com peso = {p1}, nota 2 = {y} com peso = {p2}, e nota 3 = {z} com peso = {p3}, o valor da media final é = {media}. Portanto, você reprovou')

print("boa")