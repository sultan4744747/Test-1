
import random
while True:
    def lox():
        print('Привет, это игра угадайка!Попробуй угадать число))')
        print('С какого по какое число ты хочешь угадать?')
        a = int(input('Введи начальное число: '))
        b = int(input('Введи конечное число: '))
        prog = random.randint(a, b)
        cnt = 1

        ya = int(input('Попробуй угадать число: : '))
        if ya > prog:
            print('Число большое! Попробуй еще раз) ')
            cnt += 1
        elif ya < prog:
            print('Число маленькое! Попробуй еще раз): ')
            cnt += 1
        else:
            print('Ты угадал за', cnt, 'попыток!!!')
        if ya == prog:
            c = input('Ты хочешь попробовать снова? Да или Нет?').lower()
            if c == 'да':
                lox()
            elif c == 'нет':
                print(" ну и пошол нах отсюда")
                quit()


                
    lox()

