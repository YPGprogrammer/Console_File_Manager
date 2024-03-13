def personal_account():
    balance = 0
    purchases = {}

    while True:
        print('1. вывести баланс счета')
        print('2. пополнение счета')
        print('3. покупка')
        print('4. история покупок')
        print('5. выход')

        user_choice = int(input('Выберите пункт меню: '))
        if user_choice == 1:
            print('Баланс вашего счёта:', balance)
        elif user_choice == 2:
            add_balance = int(input('Введите сумму пополнения счета: '))
            if add_balance < 1:
                print('Неверная сумма пополнения!')
            else:
                balance += add_balance
                print('Баланс пополнен на', add_balance)
        elif user_choice == 3:
            purchase_sum = int(input('Введите сумму покупки: '))
            if purchase_sum > balance:
                print('Недостаточно средств на балансе!')
            else:
                purchase_thing = str(input('Введите название покупки: '))
                purchases[purchase_thing] = purchase_sum
                balance -= purchase_sum
                print('Покупка', purchase_thing, 'на', purchase_sum)
        elif user_choice == 4:
            print('История покупок:', purchases)
        else:
            break