import random
a=random.randint(1,101)

t=0
while True:
    t+=1
    h= int(input('guess yor number between 1-100: '))
    

    if h==a:
        print(f'congratulation you have won this game in {t} tries, the number is {a}')
        break

    elif h>a:
        print('wrong number, please go lower ')
    elif h<a:
        print('wrong number, please go higher')