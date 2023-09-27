while True:
    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)
    except Exception as e:
        print('Yanlış bir değer girdiniz.',e)
    else:
        break
    finally:
        print('try except sonlandı.')