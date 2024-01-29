"""Module providing a function printing python version."""
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('Yanlış bilgi girdiniz')
        print(e)
    else:
        break    