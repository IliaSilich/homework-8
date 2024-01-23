def vending_machine(drinks):
    print("Выберите напиток:")
    for drink, price in drinks.items():
        print(f"{drink} - {price} руб.")
    user_choice = yield

    while True:
        if user_choice not in drinks:
            print("Некорректный выбор. Пожалуйста, выберите напиток из списка.")
            user_choice = yield
            continue

        selected_drink = user_choice
        drink_price = drinks[selected_drink]
        print(f"Вы выбрали {selected_drink}. Внесите {drink_price} руб.")
        user_payment = yield

        if user_payment < drink_price:
            print("Недостаточно денег.")
        else:
            change = user_payment - drink_price
            print(f"Ваш напиток {selected_drink} готов. Заберите и сдача {change} руб.")
            user_choice = yield


drinks_dict = {'coffe': 10, 'cola': 20}
vm = vending_machine(drinks_dict)
next(vm)
vm.send('cola')
vm.send(10)
vm.send(20)
vm.send('tea')
vm.send('coffe')
vm.send(30)
